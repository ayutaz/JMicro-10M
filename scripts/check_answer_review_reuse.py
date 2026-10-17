"""Check exact historical evidence reuse and reject near matches, no model work."""
import copy
from pathlib import Path
from answer_learning_common import ROOT,RUN as PARENT_RUN,save,ref,bound,read_json,now
from review_answer_curriculum import wire,historical_index,POLICY
from run_answer_curriculum_resource_v2 import RUN
import review_chat_natural as original


def main():
    target=PARENT_RUN/'exact_review_reuse_CPU_checks.json';assert not target.exists()
    policy=read_json(POLICY);old_root=ROOT/'reports/phase7/chat-natural-sft-20261017/evaluation'
    assert Path(policy['historical_evaluation_root'])==old_root
    before=ref(RUN/'evaluation/C0/new/notes.json');wire();index=historical_index()
    assert len(list(old_root.glob('*/*/notes.json')))==10
    assert sum(len(read_json(p)['judgments']) for p in old_root.glob('*/*/notes.json'))==2190
    _,_,items=original.get_items(RUN/'evaluation/C0/new/result.json');item=next(iter(items.values()))
    baseline=original.fingerprint(item);checks={'identical_copy':original.fingerprint(copy.deepcopy(item))==baseline}
    for label,change in [
        ('history',lambda x:x['messages'][-1].__setitem__('content',x['messages'][-1]['content']+' ')),
        ('checks',lambda x:x['checks'].append('Different condition')),
        ('category',lambda x:x.__setitem__('category','different')),
        ('generated_IDs',lambda x:x['response']['generated_ids'].append(8)),
        ('raw_bytes',lambda x:x['response'].__setitem__('raw_bytes_hex',x['response']['raw_bytes_hex']+'00')),
        ('text',lambda x:x['response'].__setitem__('text',x['response']['text']+' ')),
        ('stop',lambda x:x['response'].__setitem__('stop_reason','different')),
        ('prompt_IDs',lambda x:x['response']['prompt_ids'].append(8)),
        ('UTF8',lambda x:x['response'].__setitem__('valid_utf8',not x['response']['valid_utf8'])),
        ('empty',lambda x:x['response'].__setitem__('empty_response',not x['response']['empty_response'])),
        ('role_leak',lambda x:x['response'].__setitem__('role_leak',not x['response']['role_leak']))]:
        changed=copy.deepcopy(item);change(changed);checks['reject_changed_'+label]=original.fingerprint(changed)!=baseline
    packet=read_json(RUN/'evaluation/C0/previous_new/packet.json')
    _,_,current=original.get_items(RUN/'evaluation/C0/previous_new/result.json');external=0
    for key,value in packet['reused'].items():
        if 'source_notes' in value and Path(value['source_notes']['path']).is_relative_to(old_root):
            fp=original.fingerprint(current[key]);assert fp==value['fingerprint'] and fp in index
            note=next(n for n in read_json(bound(value['source_notes']))['judgments'] if n['key']==value['source_notes']['key'])
            assert all(note[k]==value[k]==index[fp][k] for k in ('grammar','relevance','context','rationale'));external+=1
    checks['actual_historical_matches_verified']=external>0
    checks['existing_C0_new_notes_unchanged']=before==ref(RUN/'evaluation/C0/new/notes.json')
    checks['new_packet_binds_policy_and_adapter']=packet['exact_reuse_policy']==ref(POLICY) and packet['review_adapter']==ref(ROOT/'scripts/review_answer_curriculum.py')
    assert all(checks.values())
    save(target,dict(status='passed',created_at=now(),checks=checks,total=len(checks),historical_validated_judgments=2190,
        historical_unique_exact_fingerprints=len(index),actual_first_packet_historical_reuse=external,
        unchanged_current_notes=before,policy=ref(POLICY),adapter=ref(ROOT/'scripts/review_answer_curriculum.py'),source=ref(__file__),
        semantic_scores_not_inferred=True,new_GPU_or_model_inference=0,new_TEST_body_read=False))
    print('Exact reuse checks passed: '+str(len(checks))+'; actual old matches='+str(external))


if __name__=='__main__':main()
