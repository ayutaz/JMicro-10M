"""One fixed decoder comparison, all 20 short/gold/single-field families."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import time
from chat_quality_100 import ROOT,read,save,sha,now
from answer_curriculum_chat_demo import Engine
from jmicro.chat_evaluation import generate_reply
from torch.nn.attention import sdpa_kernel,SDPBackend

RUN=ROOT/'reports/phase7/chat-recovery-20261018'


def main():
    target=RUN/'sampling_raw.json';protocol=RUN/'sampling_protocol.json'
    assert not target.exists() and not protocol.exists()
    inputs=[r for r in read(RUN/'history/inputs.json')['rows'] if (r['query_turn'],r['field_count'],r['history_quality'])==(3,'one','gold')]
    assert len(inputs)==20
    save(protocol,dict(created_at=now(),inputs_sha256=sha(RUN/'history/inputs.json'),source_sha256=sha(__file__),
        selected_ids=[r['id'] for r in inputs],selection='All20 families in a fixed condition; no success/failure selection',
        specification=dict(temperature=.7,top_p=.9,top_k=0,seeds=[41,42,43],max_new_tokens=32),
        wall_limit=1800,checkpoint='b5cb947c2d580e8ec4a080cfa71571a5e59baa2d24272c4229634799c913bc61',
        gate='Conditional auxiliary comparison: some correct-answer divergence tokens compete within top10 in prior likelihood assay; no decoder search',
        all_outputs_required=True,no_training=True))
    engine=Engine('C1');started=time.monotonic()
    report=dict(status='running',created_at=now(),protocol_sha256=sha(protocol),model=engine.info,rows=[])
    save(target,report)
    def check():assert time.monotonic()-started<1800
    try:
        with sdpa_kernel(SDPBackend.MATH):
            for row in inputs:
                for seed in (41,42,43):
                    answer=generate_reply(engine.model,engine.tok,row['messages'],'cpu','fp32',32,True,check,
                        sampling=dict(seed=seed,temperature=.7,top_p=.9,top_k=0))
                    report['rows'].append(dict(input_id=row['id'],family=row['family'],seed=seed,expected=row['expected'],messages=row['messages'],response=answer))
                    save(target,report)
        assert len(report['rows'])==60
        report.update(status='complete_pending_all_literal_review',CPU_wall_seconds=time.monotonic()-started)
    except BaseException as error:
        report.update(status='failed_partial_preserved',error=repr(error));raise
    finally:save(target,report)


if __name__=='__main__':main()
