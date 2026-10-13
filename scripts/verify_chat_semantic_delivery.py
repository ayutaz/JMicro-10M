"""CPU-only portable archive/document delivery checks for the closed comparison."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from chat_semantic_contract import RUN, reference

WINDOWS = Path('/mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m')
GIT = '/mnt/c/Program Files/Git/cmd/git.exe'
RELATIVE = RUN.relative_to(ROOT)
DOCUMENTS = ('AGENTS.md', 'README.md', 'docs/autonomous_status.md',
             'docs/15_project_roadmap.md', 'docs/windows_handoff.md', 'docs/README.md',
             'docs/10_next_steps.md', 'docs/124_base_recovery_plan.md',
             'docs/135_chat_problem_solution_plan.md',
             'docs/137_chat_semantic_diversity_execution.md',
             'docs/138_chat_semantic_diversity_results.md')


def git(*args):
    # Windows remains authoritative; use Windows Git without touching WSL Git.
    output = subprocess.run([GIT, '-C', r'C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m', *args],
                            check=True, capture_output=True)
    return output.stdout.decode('utf-8').strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--result-commit')
    args = parser.parse_args()
    config_path = ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json'
    # Scientific preflight already passed. Delivery verifies its frozen bytes;
    # it does not repeat full TRAIN/data preparation or GPU diagnostics.
    config = dict(read_json(config_path), config_sha256=sha256(config_path), config_path=str(config_path))
    completion = read_json(RUN / 'completion.json')
    assert completion['config'] == reference(config_path)
    assert completion['all_six_steps_complete'] and completion['scope_complete']
    assert completion['eligible_candidate'] is None
    assert not completion['model_quality_complete']
    assert completion['documentation_delivery_and_commit_still_required'] is True
    assert completion['GPU_total_seconds'] < completion['GPU_limit_seconds'] == 21600
    selection = read_json(RUN / 'selection.json')
    assert not selection['candidate_eligible'] and selection['eligible_candidate'] is None
    assert selection['new_joint_CI_lower'] == -.0875
    progress = read_json(RUN / 'progress_audit.json')
    assert (progress['reviewed_suites'], progress['content_judgments'], progress['fixed_NLL_points']) == (21, 4599, 7)
    assert progress['pending'] == []
    tests = read_json(RUN / 'completion_gate_checks.json')
    assert tests['passed']
    archive = read_json(RUN / 'final_archive.json')
    assert archive['config_sha256'] == config['config_sha256']
    assert archive['weights_and_datasets_in_git'] is False
    paths = {entry['path'] for entry in archive['files']}
    assert len(paths) == len(archive['files'])
    for entry in archive['files']:
        win, linux = WINDOWS / entry['path'], ROOT / entry['path']
        assert win.is_file() and linux.is_file(), entry['path']
        assert sha256(win) == sha256(linux) == entry['sha256'], entry['path']
        assert win.stat().st_size == entry['bytes'], entry['path']
        assert win.suffix in ('.json', '.md', '.tsv', '.py', '.ps1') or win.name == 'metrics.jsonl'
        assert win.suffix != '.pt'
    for source, digest in config['source_sha256'].items():
        assert sha256(WINDOWS / source) == sha256(ROOT / source) == digest, source
    history = read_json(RUN / 'documentation_history/baseline.json')
    for entry in history['files']:
        assert sha256(WINDOWS / entry['archive']) == sha256(ROOT / entry['archive']) == entry['sha256']
    destination = WINDOWS / RELATIVE / 'final_delivery_checks.json'
    links = 0
    for name in DOCUMENTS:
        doc = WINDOWS / name
        assert name in paths and sha256(doc) == sha256(ROOT / name)
        text = doc.read_text(encoding='utf-8')
        assert '138' in text, name
        for match in re.finditer(r'\[[^\]\n]*\]\(([^)\n]+)\)', text):
            target = match.group(1).split('#', 1)[0].strip('<>')
            if not target or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                continue
            local = (doc.parent / target).resolve()
            assert local.is_relative_to(WINDOWS.resolve()), (name, target)
            assert local.is_file() or local == destination.resolve(), (name, target)
            links += 1
    result_text = (WINDOWS / 'docs/138_chat_semantic_diversity_results.md').read_text(encoding='utf-8')
    for literal in ('19 | 12 | 21 | 15 | 11', '−8.75〜+16.25',
                    '3,646', '1,899,557', '2,443.007', '不正UTF8', 'Codex非blind'):
        assert literal in result_text, literal
    assert '未再開' in (WINDOWS / 'docs/135_chat_problem_solution_plan.md').read_text(encoding='utf-8')
    assert 'completed and stopped' in (WINDOWS / 'AGENTS.md').read_text(encoding='utf-8')
    subprocess.run([GIT, '-C', r'C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m',
                    'diff', '--check'], check=True, capture_output=True)
    assert git('config', '--local', 'user.name') == 'yousan'
    assert git('config', '--local', 'user.email') == 'ka1357amnbpdr@gmail.com'
    result_commit = None
    if args.result_commit:
        result_commit = git('rev-parse', args.result_commit + '^{commit}')
        for entry in archive['files']:
            subprocess.run([GIT, '-C', r'C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m',
                            'cat-file', '-e', result_commit + ':' + entry['path']],
                           check=True, capture_output=True)
        # Every portable file is tracked unchanged. Only this receipt may be new.
        untracked = git('ls-files', '--others', '--exclude-standard')
        assert not untracked, untracked
        changed = git('diff', '--name-only').splitlines()
        assert set(changed) <= {str(RELATIVE / 'final_delivery_checks.json')}, changed
        assert git('diff', '--cached', '--name-only') == ''
    output = dict(passed=True, completed_at=now(), verification_source=reference(Path(__file__)),
                  config=reference(Path(config['config_path'])), scientific_completion=reference(RUN / 'completion.json'),
                  archive=reference(RUN / 'final_archive.json'), file_count=len(paths),
                  all_portable_bytes_match_Windows_and_WSL=True, frozen_sources_unchanged=True,
                  preserved_document_history_verified=True, local_document_links_verified=links,
                  document_state_and_final_counts_verified=True, git_diff_check_passed=True,
                  result_commit=result_commit, documentation_report_and_archive_complete=True,
                  result_commit_verified=result_commit is not None,
                  final_receipt_commit_still_required=True,
                  stopped_after_requested_six_stages=True, additional_research_launched=False,
                  Base_adopted=False, Chat_adopted=False, push_executed=False, publication_executed=False,
                  quality_limitations='Codex nonblind; reused control; no qualified retention/sampling or independent final confirmation.')
    atomic_json(RUN / 'final_delivery_checks.json', output)
    print(json.dumps({key: output[key] for key in ('passed', 'file_count', 'local_document_links_verified',
                                                  'result_commit_verified', 'stopped_after_requested_six_stages')}))


if __name__ == '__main__':
    main()
