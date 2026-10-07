"""JSON tuple/list record adapter for the frozen gate reviewer; gates unchanged."""
import argparse
from contextlib import contextmanager
import json
from pathlib import Path
import shutil
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json
from phase6_performance import alive
import review_base_headwise_gate as original

PREPARATION=original.RUN/'review-JSON-spec-v2-preparation.json'


def normalized_record(state,record):
    """Check exact JSON representation before restoring PT specification types."""
    if json.loads(json.dumps(state['spec'],allow_nan=False))!=record['spec']:
        raise ValueError('Recorded JSON gate specification differs from actual PT state')
    return dict(record,spec=state['spec'])


@contextmanager
def adapted_audit():
    previous=original.audit_state
    def audit(state,record,*args,**kwargs):
        return previous(state,normalized_record(state,record),*args,**kwargs)
    original.audit_state=audit
    try:yield
    finally:original.audit_state=previous


def prepare():
    if PREPARATION.exists():raise ValueError('Preserve prospective reviewer adapter evidence')
    c,p=original.load_policy();job=read_json(original.RUN/'job.json')
    if not alive(job) or job['status']!='running':raise ValueError('Own actual science must be live')
    if any(original.raw_path(a).exists() for a in original.ARMS):
        raise ValueError('Record metadata-only repair before current quality outcomes')
    state=dict(spec=dict(kind='metadata_fixture',optimizer_recipe=dict(betas=(.9,.999),lr=1e-5)))
    record=json.loads(json.dumps(state));before=json.dumps(record,sort_keys=True)
    if state['spec']==record['spec']:raise ValueError('Expected actual PT/JSON tuple-list difference absent')
    normalized=normalized_record(state,record)
    if normalized['spec']!=state['spec'] or json.dumps(record,sort_keys=True)!=before:
        raise ValueError('Exact-value normalization failed or original record changed')
    modified=json.loads(before);modified['spec']['optimizer_recipe']['betas'][1]=.998
    try:normalized_record(state,modified)
    except ValueError as error:refusal=str(error)
    else:raise ValueError('Changed optimizer recipe accepted')
    copied=[];previous=original.audit_state
    def fixture_audit(actual,converted,*args,**kwargs):
        copied.append(converted['spec']==actual['spec']);raise RuntimeError('fixture downstream error')
    original.audit_state=fixture_audit
    try:
        try:
            with adapted_audit():original.audit_state(state,record)
        except RuntimeError as error:
            if str(error)!='fixture downstream error':raise
        if copied!=[True] or original.audit_state is not fixture_audit:
            raise ValueError('Adapter dispatch/exception restoration failed')
    finally:original.audit_state=previous
    destination=original.RUN/'source/scripts'/Path(__file__).name
    destination.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(Path(__file__),destination)
    atomic_json(PREPARATION,dict(created_at=now(),status='reviewer_JSON_metadata_adapter_prepared_not_quality',
        source=dict(path=str(Path(__file__)),sha256=sha256(Path(__file__))),
        original_reviewer_sha256=sha256(Path(original.__file__)),
        config_sha256=sha256(original.CONFIG),policy_sha256=sha256(original.POLICY),
        actual_live_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
        PT_JSON_difference_reproduced=True,exact_JSON_values_required=True,original_record_unchanged=True,
        changed_beta_rejected=refusal,adapter_exception_restore_verified=True,
        scientific_source_changed=False,optimizer_recipe_changed=False,quality_criteria_changed=False,
        new_generation_read=0,GPU_seconds=0,Base_complete=False,Chat_started=False,quantization_started=False))
    print('Exact PT/JSON spec adapter verified; changed beta refused; scientific source/criteria unchanged; quality0/GPU0')


def review(template=False):
    evidence=read_json(PREPARATION)
    if (evidence['source']['sha256']!=sha256(Path(__file__))
            or evidence['original_reviewer_sha256']!=sha256(Path(original.__file__))
            or evidence['config_sha256']!=sha256(original.CONFIG) or evidence['policy_sha256']!=sha256(original.POLICY)
            or evidence['quality_criteria_changed'] or evidence['scientific_source_changed']):
        raise ValueError('Preserved exact metadata-only review adapter required')
    with adapted_audit():original.review(template)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__);group=parser.add_mutually_exclusive_group()
    group.add_argument('--prepare',action='store_true');group.add_argument('--template',action='store_true');args=parser.parse_args()
    prepare() if args.prepare else review(args.template)
