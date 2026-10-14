"""Verify actual rejected-study delivery; do not infer Base quality completion."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime,timezone
from urllib.request import urlopen

ROOT=Path(__file__).resolve().parents[1]
WIN=Path('/mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m')
WIN_GIT_ROOT=r'C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m'
GIT='/mnt/c/Program Files/Git/cmd/git.exe'
RUN=ROOT/'reports/phase6/base-document-balance-comparison-20261014'
BASELINE='70aa00299173d0d8ffcce38a49055c88a0810f62'
DOCS=('AGENTS.md','README.md','docs/README.md','docs/autonomous_status.md',
    'docs/15_project_roadmap.md','docs/windows_handoff.md',
    'docs/124_base_recovery_plan.md','docs/143_base_document_balance_plan.md','docs/144_base_document_balance_results.md')
sys.path.insert(0,str(Path(__file__).resolve().parent))
from observe_base_document_balance import live


def read(path): return json.loads(path.read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def git(*args): return subprocess.run([GIT,'-C',WIN_GIT_ROOT,*args],check=True,capture_output=True).stdout.decode().strip()


def verify(commit=None,receipt_commit=None):
    manifest=read(RUN/'local_archive_manifest.json')
    assert manifest['files_count']==len(manifest['files'])==40
    for record in manifest['files']:
        p=record['path']
        assert sha(ROOT/p)==sha(WIN/p)==record['sha256'],p
    assert not manifest['datasets_copied'] and not manifest['weights_copied_to_Git'] and not manifest['samplers_copied_to_Git']
    completion=read(ROOT/'reports/phase6/base_document_balance_comparison_completion.json')
    review=read(ROOT/'reports/phase6/base_document_balance_comparison_review.json')
    numeric=read(RUN/'numeric_completion_audit.json')
    config=read(ROOT/'configs/phase6/base_document_balance_comparison.json')
    assert numeric['passed'] and sha(Path(numeric['source']['path']))==numeric['source']['sha256']
    assert numeric['full_checkpoint_sha256']==manifest['native_final_checkpoint']['sha256']
    assert sha(Path(manifest['native_final_checkpoint']['path']))==manifest['native_final_checkpoint']['sha256']
    assert numeric['history']['all_committed_updates']==17698 and numeric['history']['actual_original_teacher_positions']==100000000
    assert completion['fixed_condition_closed'] and completion['comparison_and_required_conditional_decisions_complete']
    assert completion['all_six_stages_actually_executed'] is False and completion['requested_quality_end_state_achieved'] is False
    assert not completion['Base_complete'] and not completion['Base_adopted']
    assert review['eligible_for_final_Base_validation'] is False
    assert not review['matched_objective_quality']['passed'] and not review['quality_comparison']['passed']
    assert not all(review['absolute_dev_screen'].values()) and not all(review['original_Web'].values())
    assert set(completion['qualified_only_branches'])=={'main_comparison','independent_fresh_trained_seed43','fullDEV_and_400_plus40','sealed_TEST','adoption'}
    assert all(r['executed'] is False and r['passed'] is False and r['quality_unconfirmed'] is True and r['reason'] for r in completion['qualified_only_branches'].values())
    notes=read(ROOT/'reports/phase6/base_document_balance_notes.json')
    raw=read(RUN/'evaluation/document_balance/evaluation/generation.json')
    assert notes['all80_individually_read'] and not notes['independent_human_blind']
    scores=notes['notes']
    assert len(scores)==len(raw['outputs'])==80 and {r[0] for r in scores}=={r['id'] for r in raw['outputs']}
    assert all(len(r[5].strip())>=12 for r in scores)
    s=review['summaries']['document_balance']
    assert (s['grammar2'],s['relevance2'],s['coherent'],s['appropriate'])==tuple(sum(r[i]==2 for r in scores) for i in (1,2,3))+(sum(r[4] for r in scores),)
    assert (s['grammar2'],s['coherent'],s['appropriate'],s['rates']['eos'],s['rates']['repetition'])==(23,1,2,20,50)
    assert review['notes_sha256']==sha(ROOT/'reports/phase6/base_document_balance_notes.json')
    assert notes['generation_sha256']==sha(RUN/'evaluation/document_balance/evaluation/generation.json')
    incident=read(RUN/'original_TEST_prompt_exposure.json')
    assert incident['unique_original_TEST_prompt_rows']==20 and not incident['original_TEST_prompts_can_be_called_unread']
    assert incident['new_sealed_Base_TEST_required_if_qualified'] and not incident['TEST_used_for_learning'] and not incident['TEST_used_for_GPU_scoring']
    assert not incident['original_TEST_shards_opened']
    assert completion['total_new_GPU_seconds']==1483.5300504029728 and completion['new_GPU_seconds']<=3855
    assert sha(ROOT/'src/jmicro/model.py')=='298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83'
    for p,digest in config['source_sha256'].items(): assert sha(ROOT/p)==sha(WIN/p)==digest,p
    link_count=0
    for p in DOCS:
        assert sha(ROOT/p)==sha(WIN/p),p
        value=(WIN/p).read_text(encoding='utf-8-sig')
        assert '\x00' not in value and '\ufffd' not in value,p
        for target in re.findall(r'\]\(([^)]+)\)',value):
            if target.startswith(('http:','https:','app:','#')): continue
            path=target.split('#',1)[0].strip('<>')
            if not path: continue
            assert ((WIN/p).parent/path).exists(),(p,target)
            link_count+=1
    ui_record=read(ROOT/'reports/local/webui/server.json')
    assert live(ui_record) and not live(read(RUN/'job.json'))
    with urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response: ui=json.load(response)
    assert ui['parameters']==10001152 and ui['checkpoint_sha256']==config['parent']['sha256'] and ui['busy'] is False
    assert git('config','--local','user.name')=='yousan'
    assert git('config','--local','user.email')=='ka1357amnbpdr@gmail.com'
    proof=dict(passed=True,verified_at=datetime.now(timezone.utc).isoformat(),
        original100M_and_all17698_update_audit_verified=True,all80_manual_judgments_verified=True,
        rejected_quality_and_all_five_conditional_decisions_verified=True,
        all_six_stages_actually_executed=False,Base_complete=False,Base_adopted=False,
        TEST_prompt_CPU_exposure_preserved=True,TEST_GPU_scoring_executed=False,
        original_native10M_source_unchanged=True,Windows_WSL_archived_files_verified=40,
        local_document_links_verified=link_count,original_WebUI_live_and_correct=True,
        scientific_process_exited=True,weights_and_full_sampler_native_only=True,
        datasets_or_TEST_parsed_by_verifier=False,new_GPU_work=False,push_executed=False,
        source_sha256=sha(Path(__file__)))
    output=RUN/'pre_delivery_checks.json'
    if commit:
        revision=git('rev-parse',commit+'^{commit}')
        assert not git('status','--porcelain'), 'Authoritative Windows worktree must be clean'
        paths=git('diff','--name-only',BASELINE,revision).splitlines()
        assert paths
        for p in paths:
            assert git('rev-parse',revision+':'+p)==git('hash-object','--path='+p,str(WIN_GIT_ROOT+'\\'+p.replace('/','\\'))),p
        proof.update(result_commit=revision,all_changed_Git_objects_verified=len(paths),committed_contents_verified=True)
        output=RUN/'final_delivery_checks.json'
        if receipt_commit:
            old=read(output)
            assert old['passed'] and old['result_commit']==revision
            assert old['source_sha256']==sha(Path(__file__))
            receipt=git('rev-parse',receipt_commit+'^{commit}')
            assert git('rev-parse','HEAD')==receipt
            p=output.relative_to(ROOT).as_posix()
            assert sha(output)==sha(WIN/p)
            assert git('rev-parse',receipt+':'+p)==git('hash-object','--path='+p,WIN_GIT_ROOT+'\\'+p.replace('/','\\'))
            proof.update(receipt_commit=receipt,local_delivery_complete=True)
            print(json.dumps(proof,ensure_ascii=False)); return
    output.write_text(json.dumps(proof,indent=2,ensure_ascii=False)+'\n')
    shutil.copyfile(output,WIN/output.relative_to(ROOT))
    print(json.dumps(proof,ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser()
    parser.add_argument('--commit');parser.add_argument('--receipt-commit')
    args=parser.parse_args()
    verify(args.commit,args.receipt_commit)
