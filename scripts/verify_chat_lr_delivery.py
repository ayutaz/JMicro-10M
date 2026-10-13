"""Verify portable final low-LR evidence against WSL, Windows and actual Git blobs."""
import argparse
import json
from pathlib import Path
import re
import subprocess

from chat_lr_contract import ROOT, RUN, reference, TOTAL, LIMITS
from jmicro.experiment import read_json, sha256, now
from jmicro.training import atomic_json

WINDOWS = Path('/mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m')
GIT = '/mnt/c/Program Files/Git/cmd/git.exe'
WIN_ROOT = r'C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m'
RELATIVE = RUN.relative_to(ROOT)
DOCUMENTS = ('AGENTS.md', 'README.md', 'docs/autonomous_status.md',
    'docs/15_project_roadmap.md', 'docs/windows_handoff.md', 'docs/README.md',
    'docs/10_next_steps.md', 'docs/124_base_recovery_plan.md',
    'docs/139_chat_lr_comparison_plan.md', 'docs/140_chat_lr_comparison_execution.md',
    'docs/141_chat_lr_comparison_results.md')


def git(*args):
    result = subprocess.run([GIT, '-C', WIN_ROOT, *args], check=True, capture_output=True)
    return result.stdout.decode('utf-8').strip()


def evidence():
    config_path = ROOT / 'configs/phase7/chat-lr-20261014.json'
    config = read_json(config_path)
    digest = sha256(config_path)
    completion = read_json(RUN / 'completion.json')
    assert completion['config'] == reference(config_path)
    assert completion['all_three_step_decisions_complete']
    assert completion['all28_suites_6132_judgments_verified'] and completion['all7_NLL_2634_targets_verified']
    assert completion['eligible_candidate'] is None and not completion['model_quality_complete']
    assert completion['documentation_archive_and_commit_still_required']
    for name in ('scope', 'intervention', 'progress', 'selection', 'analysis', 'conditional_branches', 'technical', 'training', 'GPU_ledger', 'source'):
        ref = completion[name]
        assert sha256(Path(ref['path'])) == ref['sha256'], name
    progress = read_json(RUN / 'progress_audit.json')
    assert (progress['reviewed_suites'], progress['content_judgments'], progress['fixed_NLL_points']) == (28, 6132, 7)
    # This immutable snapshot was taken immediately before branch/completion
    # creation; their current references above prove the formerly pending work.
    assert set(progress['pending']) == {'conditional_branches.json', 'completion.json'}
    selection = read_json(RUN / 'selection.json')
    assert selection['point'] == 't3' and selection['eligible_candidate'] is None
    assert not selection['candidate_eligible'] and selection['new_joint_CI_lower'] == -.0125
    assert not selection['Base_adopted'] and not selection['Chat_adopted']
    for suite, content, context in (('new',20,5),('semantic',18,5),('previous',19,5),('old',15,1)):
        row = selection['summary']['S1'][suite]
        assert row['content']['primary']['joint_grammar_relevance_score2'] == content
        assert row['content']['own_history_final24']['context_score2'] == context
        assert not row['absolute_passed']
    branches = read_json(RUN / 'conditional_branches.json')['branches']
    assert set(branches) == {'Base_retention','sampling','independent_learning_seed43','human_blind','fullDEV','sealed_TEST','adoption'}
    assert all(row == dict(status='skipped_no_eligible_candidate', executed=False, passed=False, quality_unconfirmed=True)
               for row in branches.values())
    ledger = read_json(RUN / 'GPU_ledger.json')
    assert ledger['limits'] == LIMITS and ledger['total_limit'] == TOTAL == 33600
    assert ledger['total_charged_seconds'] == completion['GPU_total_seconds']
    assert all(row['status'] == 'complete' for row in ledger['entries'])
    tests = read_json(RUN / 'completion_gate_checks.json')
    assert tests['passed'] and tests['CPU_checks'] == 20 and tests['config_sha256'] == digest
    for ref in tests['sources'].values():
        assert sha256(Path(ref['path'])) == ref['sha256']
    assert tests['actual_selection'] == reference(RUN / 'selection.json')
    assert tests['actual_NLL'] == reference(RUN / 'NLL/S1/t3.json')
    return config_path, config, digest, completion


def build(config_path, config, digest):
    paths = {str(p.relative_to(ROOT)) for p in RUN.rglob('*') if p.is_file() and
             (p.suffix in ('.json','.tsv','.md','.py','.ps1') or p.name == 'metrics.jsonl') and
             p.name not in ('final_archive.json','final_delivery_checks.json')}
    paths.update(str(p.relative_to(ROOT)) for p in (ROOT / 'scripts').glob('*chat_lr*') if p.suffix in ('.py','.ps1'))
    paths.update(config['source_sha256'])
    paths.update(DOCUMENTS)
    paths.update(('.gitattributes', str(config_path.relative_to(ROOT))))
    rows = []
    for name in sorted(paths):
        path = ROOT / name
        assert path.is_file() and path.suffix != '.pt'
        rows.append(dict(path=name, sha256=sha256(path), bytes=path.stat().st_size))
    atomic_json(RUN / 'final_archive.json', dict(config_sha256=digest, created_at=now(), files=rows,
        weights_and_datasets_in_git=False, numerical_state_in_WSL=True,
        weights=read_json(RUN / 'S1/checkpoints.json'),
        datasets={key: config[key] for key in ('TRAIN_manifest','fixed_NLL')},
        build_source=reference(Path(__file__))))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--build', action='store_true')
    parser.add_argument('--result-commit')
    parser.add_argument('--receipt-commit')
    args = parser.parse_args()
    config_path, config, digest, completion = evidence()
    if args.build:
        assert not args.result_commit and not args.receipt_commit
        build(config_path, config, digest)
        print('Portable manifest built; mirror and commit before final delivery certification')
        return
    archive = read_json(RUN / 'final_archive.json')
    assert archive['config_sha256'] == digest and not archive['weights_and_datasets_in_git']
    assert archive['build_source'] == reference(Path(__file__))
    paths = {row['path'] for row in archive['files']}
    assert len(paths) == len(archive['files'])
    for row in archive['files']:
        win, linux = WINDOWS / row['path'], ROOT / row['path']
        assert win.is_file() and linux.is_file(), row['path']
        assert sha256(win) == sha256(linux) == row['sha256'], row['path']
        assert win.stat().st_size == linux.stat().st_size == row['bytes'], row['path']
    assert sha256(WINDOWS / RELATIVE / 'final_archive.json') == sha256(RUN / 'final_archive.json')
    for source, expected in config['source_sha256'].items():
        assert sha256(WINDOWS / source) == sha256(ROOT / source) == expected, source
    for entry in read_json(RUN / 'documentation_history/baseline.json')['files']:
        assert sha256(WINDOWS / entry['archive']) == sha256(ROOT / entry['archive']) == entry['sha256']
    links = 0
    receipt_relative = str(RELATIVE / 'final_delivery_checks.json')
    receipt_path = WINDOWS / receipt_relative
    for name in DOCUMENTS:
        assert name in paths
        doc = WINDOWS / name
        content = doc.read_text(encoding='utf-8')
        assert '141' in content, name
        for match in re.finditer(r'\[[^\]\n]*\]\(([^)\n]+)\)', content):
            target = match.group(1).split('#', 1)[0].strip('<>')
            if not target or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                continue
            local = (doc.parent / target).resolve()
            assert local.is_relative_to(WINDOWS.resolve()), (name, target)
            assert local.is_file() or local == receipt_path.resolve(), (name, target)
            links += 1
    result_text = (WINDOWS / 'docs/141_chat_lr_comparison_results.md').read_text(encoding='utf-8')
    for literal in ('13 | 20 | 3 | 5', '−1.25〜+18.75', '3,646', '1,899,557',
                    '2,658.673', '不正UTF8', 'Codex非blind', '未実行'):
        assert literal in result_text, literal
    assert 'completed and stopped' in (WINDOWS / 'AGENTS.md').read_text(encoding='utf-8')
    assert git('config','--local','user.name') == 'yousan'
    assert git('config','--local','user.email') == 'ka1357amnbpdr@gmail.com'
    git('diff','--check')
    assert args.result_commit, 'Final result commit required'
    result_commit = git('rev-parse',args.result_commit + '^{commit}')
    for name in sorted(paths | {str(RELATIVE / 'final_archive.json')}):
        win_path = WIN_ROOT + '\\' + name.replace('/', '\\')
        expected_oid = git('hash-object','--path='+name,win_path)
        assert git('rev-parse', result_commit + ':' + name) == expected_oid, name
    assert not git('ls-files','--others','--exclude-standard')
    assert not git('diff','--name-only') and not git('diff','--cached','--name-only')
    output = dict(passed=True, completed_at=now(), source=reference(Path(__file__)),
        config=reference(config_path), scientific_completion=reference(RUN / 'completion.json'),
        archive=reference(RUN / 'final_archive.json'), result_commit=result_commit, file_count=len(paths),
        all_portable_bytes_match_Windows_and_WSL=True, frozen_sources_unchanged=True,
        preserved_document_history_verified=True, local_document_links_verified=links,
        committed_file_contents_verified=True, documentation_report_archive_and_result_commit_complete=True,
        receipt_commit_still_required=True, all_three_requested_decisions_complete=True,
        model_quality_complete=False, independent_confirmation_executed=False,
        independent_quality_unconfirmed=True, Base_adopted=False, Chat_adopted=False,
        additional_research_launched=False, push_executed=False, publication_executed=False)
    if args.receipt_commit:
        receipt = read_json(RUN / 'final_delivery_checks.json')
        assert sha256(receipt_path) == sha256(RUN / 'final_delivery_checks.json')
        assert receipt['passed'] and receipt['result_commit'] == result_commit
        receipt_commit = git('rev-parse', args.receipt_commit+'^{commit}')
        win_path = WIN_ROOT+'\\'+receipt_relative.replace('/','\\')
        assert git('rev-parse',receipt_commit+':'+receipt_relative) == git('hash-object','--path='+receipt_relative,win_path)
        assert git('rev-parse','HEAD') == receipt_commit
        print(json.dumps(dict(passed=True, result_commit=result_commit, receipt_commit=receipt_commit,
            all_three_step_scope_and_delivery_complete=True, worktree_clean=True,
            model_quality_complete=False, independent_quality_unconfirmed=True)))
        return
    atomic_json(RUN / 'final_delivery_checks.json', output)
    print(json.dumps(dict(passed=True, file_count=len(paths), result_commit=result_commit,
                         receipt_commit_still_required=True)))


if __name__ == '__main__':
    main()
