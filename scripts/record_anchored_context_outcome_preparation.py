"""Bind actual CPU preparation; this record is not learned CUDA/quality evidence."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json


def ref(path):return dict(path=str(path),sha256=sha256(path))


def main():
    sources=('scripts/anchored_context_outcome.py','scripts/anchored_context_outcome_trainer.py',
        'scripts/anchored_context_outcome_resident_trainer.py','scripts/prepare_anchored_context_outcome_trainer.py',
        'tests/test_anchored_context_outcome.py','tests/test_anchored_context_outcome_trainer.py')
    tests=ROOT/'reports/phase6/anchored_context_outcome_cpu_tests.xml'
    suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=4 or any(int(s.attrib[k]) for s in suites for k in ('errors','failures','skipped')):
        raise ValueError('All four actual CPU checks required')
    proposal=ROOT/'reports/phase6/anchored_context_outcome_proposal.json';p=read_json(proposal)
    record=dict(status='positive_anchor_CPU_loss_masks_causal_model_full_resume_passed_CUDA_pending',created_at=now(),
        proposal=ref(proposal),CPU_tests=ref(tests),CPU_passed_tests=4,
        CPU_test_seconds=sum(float(s.attrib['time']) for s in suites),
        source_sha256={r:sha256(ROOT/r) for r in sources},
        actual_checks=['Positive correct-row token-weighted loss and identical old ranking term; foil/prefix/pad/directEOS hard gradient excluded.',
            'Concrete lower-gold-probability/improved-ranking example detected by added anchor.',
            'Real tiny learned CPU model4vs2+2 matches entire saved state and all nonduration history; all3 samplers, newhard ledger and singleAdamstep preserved; corrupted teacher state rejected.',
            'Actual JMicro CPU valid logits match padded/standalone rows; future changed tokens cannot alter earlier logits.'],
        operational_failures=[dict(stage='new_owned_runner_generation_before_GPU',error='Unique-fragment guard refused incorrect newline-count before writing outputs.',
            repair='Adjusted new unfrozen builder to actual three-newline source boundary; prior frozen files unchanged.',GPU_seconds=0)],
        fixed_train_inputs=p['fixed_pair_inputs']['manifest'],new_original_corpus_tokens=0,
        GPU_training_seconds=0,scientific_teacher_tokens=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
        next_action='Own actual CUDA4vs2+2/new ledger and32 combined timings; freeze only if all probe costs plus unchanged reserves fit900 GPU seconds.')
    path=ROOT/'reports/phase6/anchored_context_outcome_preparation.json'
    if path.exists():raise ValueError('Preserve prepared positive anchor evidence')
    atomic_json(path,record);print(record['status'])


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
