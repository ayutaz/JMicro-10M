"""Correct the prospective document-head index after CPU-only implementation checks."""
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json

if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
original=ROOT/'reports/phase6/base_on_policy_teacher_proposal.json'
out=ROOT/'reports/phase6/base_on_policy_teacher_proposal_v2.json'
if out.exists():raise ValueError('Keep the corrected prospective recipe')
p=read_json(original)
p['created_at']=now();p['previous_proposal']=dict(path=str(original),sha256=sha256(original))
p['CPU_initial_failure']=dict(path=str(ROOT/'reports/phase6/base_on_policy_teacher_tests_initial_failure.xml'),
    sha256=sha256(ROOT/'reports/phase6/base_on_policy_teacher_tests_initial_failure.xml'))
p['implementation_correction']='Original sampler document_windows starts supervised body at serialized position1; BOS is position0. Initial implementation incorrectly required target_first0 and skipped all auxiliary batches; three CPU assertions rejected this. Require existing original_document_first_window and target_first1 instead, preserving intended genuine heads. No GPU/science/content results were used, no head/source/width/count/objective/budget selection or threshold change.'
p['on_policy']['prefix_selection']=p['on_policy']['prefix_selection'].replace('target_first0 and BOS2',
    'original_document_first_window=True, target_first1 and BOS2')
atomic_json(out,p)
print(json.dumps(dict(status='head_index_correction_frozen_after_CPU_failures_GPU0',sha256=sha256(out))))
