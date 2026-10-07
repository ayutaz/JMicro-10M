"""Supply only the missing stdlib math import to the preserved frozen SAM reviewer.

Original source/config/policy/results remain byte-for-byte unchanged. Every
existing history, raw-content and quality guard executes in the original code.
"""
import argparse
import math
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import review_base_sam as frozen
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json


def main(template=False):
    fix=ROOT/'reports/phase6/base_sam_reviewer_import_repair.json'
    policy=read_json(frozen.POLICY)
    expected=policy['helper_sha256']['scripts/review_base_sam.py']
    if sha256(ROOT/'scripts/review_base_sam.py')!=expected:
        raise ValueError('Preserve original frozen reviewer bytes')
    identities=dict(original_reviewer_sha256=expected,wrapper_sha256=sha256(Path(__file__)),
        scientific_result_sha256=sha256(frozen.RUN/'result.json'),config_sha256=sha256(frozen.CONFIG),
        policy_sha256=sha256(frozen.POLICY))
    if fix.exists():
        previous=read_json(fix)
        if any(previous[k]!=v for k,v in identities.items()): raise ValueError('Import repair identity changed')
    else:
        atomic_json(fix,dict(created_at=now(),**identities,
            original_failure="NameError: name 'math' is not defined",
            failed_command='uv run --frozen --extra hub --extra data --extra ml --extra export scripts/review_base_sam.py --template',
            failed_stage='Original all-history finite SAM guard; no notes or quality review created',
            repair='Bind standard-library math in original reviewer module globals only',
            original_frozen_sources_changed=False,scientific_settings_changed=False,criteria_changed=False,
            new_GPU_seconds=0,Base_complete=False,Chat_started=False,quantization_started=False))
    frozen.math=math
    frozen.review(template)
    if not template:
        target=ROOT/'reports/phase6/base_sam_comparison_review.json'
        result=read_json(target)
        result['reviewer_import_repair']=dict(path=str(fix),sha256=sha256(fix),**identities)
        atomic_json(target,result)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--template',action='store_true')
    main(parser.parse_args().template)
