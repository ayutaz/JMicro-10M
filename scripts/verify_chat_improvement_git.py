"""Read authoritative Windows Git blobs with pinned WSL uv; never publish."""
import argparse
import hashlib
import subprocess
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from chat_improvement_contract import RUN,preflight


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--final',action='store_true');args=parser.parse_args()
    win=Path('/mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m')
    assert win.is_dir()
    def git(*command):
        return subprocess.run(['git','-C',str(win),*command],check=True,capture_output=True).stdout
    config,_,_=preflight(ROOT/'configs/phase7/chat-improvement-20261012.json')
    head=git('rev-parse','HEAD').decode().strip()
    refs={'configs/phase7/chat-improvement-20261012.json':config['config_sha256']}
    for source,digest in config['source_sha256'].items():
        refs['reports/phase7/chat-improvement-20261012/source/'+source]=digest
    checked={}
    for relative,digest in refs.items():
        raw=git('show',head+':'+relative)
        assert hashlib.sha256(raw).hexdigest()==sha256(win/relative)==digest,relative
        checked[relative]=digest
    assert sha256(win/'src/jmicro/model.py')=='298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83'
    metadata={}
    run=win/'reports/phase7/chat-improvement-20261012'
    if args.final:
        completion=read_json(run/'completion.json');assert completion['scope_complete']
        for relative_bytes in git('ls-tree','-r','--name-only',head,'reports/phase7/chat-improvement-20261012').splitlines():
            relative=relative_bytes.decode();path=win/relative
            assert path.suffix not in ('.pt','.safetensors','.model','.bin')
            assert path.name not in ('train.jsonl','dev.jsonl','nll_fixed.jsonl')
            digest=hashlib.sha256(git('show',head+':'+relative)).hexdigest()
            assert sha256(path)==digest,relative
            if path.is_relative_to(run) and (ROOT/relative).exists():assert sha256(ROOT/relative)==digest,relative
            metadata[relative]=digest
    atomic_json(RUN/('final_git_verification.json' if args.final else 'intermediate_git_verification.json'),dict(
        passed=True,observed_at=now(),authoritative_windows_repository=str(win),local_HEAD=head,
        frozen_config_and_all18_source_snapshot_Git_blobs=checked,metadata_Git_blobs=metadata,
        original_windows_model_sha256=sha256(win/'src/jmicro/model.py'),publication_or_push=False,
        quality_evidence=False,source_sha256=sha256(Path(__file__))))
    print('Windows Git frozen byte bindings verified at '+head)


if __name__=='__main__':main()
