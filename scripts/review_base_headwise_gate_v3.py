"""Read CUDA BF16/Flash committed state on CPU without claiming CPU CUDA proof."""
import argparse
from contextlib import contextmanager
from pathlib import Path
import shutil
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import now,read_json,sha256
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
import review_base_headwise_gate as original
import review_base_headwise_gate_v2 as JSON_adapter

PREPARATION=original.RUN/'review-CPU-state-v3-preparation.json'


@contextmanager
def CPU_state_audit():
    previous_trainer=original.HeadwiseGateTrainer
    with JSON_adapter.adapted_audit():
        previous_audit=original.audit_state
        def cpu_reader(*args,**kwargs):
            if kwargs.get('device')!='cpu':raise ValueError('Read-only CPU state auditor required')
            trainer=previous_trainer(*args,**kwargs)
            if (trainer.spec['dtype'],trainer.spec['backend'])!=('fp32','math'):
                raise ValueError('Original CPU reader metadata changed')
            # The reader runs no forward/backward/update. Its parameters and
            # Adam tensors are FP32 on both training and reader devices. These
            # two fields describe the proven scientific training recipe.
            trainer.spec.update(dtype='bf16',backend='flash')
            return trainer
        def audit(state,record,*args,**kwargs):
            if (state['spec'].get('dtype'),state['spec'].get('backend'))!=('bf16','flash'):
                raise ValueError('Actual scientific CUDA BF16/Flash recipe required')
            return previous_audit(state,record,*args,**kwargs)
        original.HeadwiseGateTrainer=cpu_reader;original.audit_state=audit
        try:yield
        finally:
            original.HeadwiseGateTrainer=previous_trainer;original.audit_state=previous_audit


def prepare():
    if PREPARATION.exists():raise ValueError('Preserve read-only state-audit repair evidence')
    torch.set_num_threads(2);c,p=original.load_policy()
    JSON_evidence=read_json(JSON_adapter.PREPARATION)
    if JSON_evidence['source']['sha256']!=sha256(Path(JSON_adapter.__file__)):
        raise ValueError('Preserved exact JSON adapter differs')
    if original.raw_path('query_headwise').exists():
        candidate_read=False  # Existing generation is not opened by this repair.
    else:candidate_read=False
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
    tok=Tokenizer(original.ROOT/c['tokenizer']);records={};refusals={}
    for arm in original.ARMS:
        record=read_json(original.RUN/arm/'train-result.json')
        if sha256(Path(record['checkpoint']))!=record['checkpoint_sha256']:
            raise ValueError('Actual committed100M checkpoint changed')
        state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
        with JSON_adapter.adapted_audit():
            try:original.audit_state(state,record,c,arm,parent,tok)
            except ValueError as error:
                refusal=str(error)
                if refusal!='Gate recipe/arm/parent/source/config differs':raise
            else:raise ValueError('Expected CPU-vs-training metadata discrepancy absent')
        with CPU_state_audit():original.audit_state(state,record,c,arm,parent,tok)
        records[arm]=dict(checkpoint=record['checkpoint'],checkpoint_sha256=record['checkpoint_sha256'],
            update=state['counters']['update'],supervised_tokens=state['counters']['supervised_tokens'],
            all_actual_committed_state_validated_on_CPU=True)
        refusals[arm]=refusal;del state
    original_audit,original_trainer=original.audit_state,original.HeadwiseGateTrainer
    with CPU_state_audit():
        try:original.audit_state(dict(spec=dict(dtype='fp32',backend='math')),{},None)
        except ValueError as error:
            changed_refusal=str(error)
            if changed_refusal!='Actual scientific CUDA BF16/Flash recipe required':raise
        else:raise ValueError('Wrong scientific training precision accepted')
    if original.audit_state is not original_audit or original.HeadwiseGateTrainer is not original_trainer:
        raise ValueError('Auditor/factory exception restoration failed')
    destination=original.RUN/'source/scripts'/Path(__file__).name
    destination.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(Path(__file__),destination)
    atomic_json(PREPARATION,dict(created_at=now(),status='read_only_CPU_fullstate_audit_repair_verified_not_quality',
        source=dict(path=str(Path(__file__)),sha256=sha256(Path(__file__))),
        JSON_adapter_sha256=sha256(Path(JSON_adapter.__file__)),original_reviewer_sha256=sha256(Path(original.__file__)),
        config_sha256=sha256(original.CONFIG),policy_sha256=sha256(original.POLICY),
        original_CPU_metadata_refusals=refusals,actual_completed_checkpoints=records,
        wrong_scientific_precision_rejected=changed_refusal,exception_restoration_verified=True,
        static80_already_reviewed=True,candidate80_read_for_this_repair=0,
        new_forward_backward_updates=0,new_optimizer_updates=0,GPU_seconds=0,
        scientific_source_changed=False,scientific_recipe_changed=False,quality_criteria_changed=False,
        Base_complete=False,Chat_started=False,quantization_started=False,
        scope='Read saved actual CUDA states on CPU. Retains strict bf16/flash training recipe and all original fullstate checks; no CPU forward is evidence of CUDA learning.'))
    print('Both actual100M fullstates accepted by CPU reader; original precision mismatch reproduced; wrong scientific precision rejected; no GPU/update/quality change')


def review():
    evidence=read_json(PREPARATION)
    if (evidence['source']['sha256']!=sha256(Path(__file__))
            or evidence['JSON_adapter_sha256']!=sha256(Path(JSON_adapter.__file__))
            or evidence['original_reviewer_sha256']!=sha256(Path(original.__file__))
            or evidence['config_sha256']!=sha256(original.CONFIG) or evidence['policy_sha256']!=sha256(original.POLICY)
            or evidence['quality_criteria_changed'] or evidence['scientific_source_changed']):
        raise ValueError('Preserved metadata-only CPU reader required')
    with CPU_state_audit():original.review()


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--prepare',action='store_true');args=parser.parse_args()
    prepare() if args.prepare else review()
