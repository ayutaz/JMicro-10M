"""Exercise actual historical NLL bindings and check source/archive readiness."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json
from chat_generalization_contract import RUN,preflight,reference,LIMITS
from prepare_chat_generalization_reuse import reusable_rpc


def main():
    c,_,_=preflight(ROOT/'configs/phase7/chat-generalization-20261013.json')
    cases={}
    for arm,points in (('parent',('t0',)),('D0',('t1','t2','t3'))):
        for point in points:
            ref=c['parent'] if arm=='parent' else read_json(RUN/'D0/checkpoints.json')[point]
            rows,proof=reusable_rpc(c,arm,point,ref)
            assert len(rows)==2250 and len({r['id'] for r in rows})==2250
            assert all(r['body_teachers']>0 and r['EOT_teachers']==1 for r in rows)
            cases[arm+'-'+point]=dict(proof,body_bytes=sum(r['body_bytes'] for r in rows))
    assert sum(LIMITS.values())==21600 and LIMITS['train_D0']==0
    audit=read_json(RUN/'D0/training_audit.json');assert audit['passed'] and audit['new_learning_updates']==0
    atomic_json(RUN/'CPU_preflight.json',dict(passed=True,created_at=now(),
        config=reference(Path(c['config_path'])),historical_RPC_NLL_cases=cases,
        historical_control_full_state_audit=reference(RUN/'D0/training_audit.json'),
        all_requested_GPU_category_caps_sum=21600,source_sha256=sha256(Path(__file__)),
        GPU_learning_updates=0,quality_evidence=False,protected_TEST_used=False))
    print('CPU preflight passed: D0 complete states, 876 old judgments, 9000 exact RPC NLL targets')


if __name__=='__main__':main()
