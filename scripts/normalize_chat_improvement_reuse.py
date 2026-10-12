"""Normalize verified reuse metadata to frozen evaluator's exact skip contract.

Retains original files and explicit provenance outside the binding. No model,
dataset, generation or judgments change, and no new quality evidence is made.
"""
from pathlib import Path
import json
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.chat_review import content_review
from chat_improvement_contract import RUN,preflight,reference
from review_chat_improvement import get_items


def main():
    c,_,_=preflight(ROOT/'configs/phase7/chat-improvement-20261012.json')
    directory=RUN/'evaluation/parent/t0/old/greedy'
    path=directory/'result.json';evaluation,items=get_items(path)
    notes=read_json(directory/'notes.json')
    rebuilt=content_review(evaluation,sha256(path),notes,items)
    assert json.loads(json.dumps(rebuilt))==read_json(directory/'review.json')
    provenance=evaluation['reuse_provenance']
    assert provenance['core_source_SHA_identical'] and provenance['all219_raw_history_ID_bytes_verified']
    assert provenance['new_GPU_generation_seconds']==0
    expected=dict(checkpoint=c['parent']['path'],checkpoint_sha256=c['parent']['sha256'],config_sha256=c['config_sha256'],
        stage='parent-t0',tokenizer_sha256=c['tokenizer']['sha256'],suite_sha256=c['old_suite']['sha256'],
        max_new_tokens=64,model_context=1024,dtype='bf16',backend='math',decoding='greedy',
        evaluation_seeds=[42],evaluation_seed=42,source_sha256=c['source_sha256'],implementation=c['implementation'],
        scored_split='dev',protected_test_used=False,
        protocol='provided80 suppressed + provided80 unsuppressed role control +24 own-history2-4turn dialogues')
    old=evaluation['binding']
    for key in ('checkpoint_sha256','tokenizer_sha256','suite_sha256','max_new_tokens','model_context','dtype','backend',
                'decoding','evaluation_seeds','evaluation_seed','implementation'):
        assert old[key]==expected[key],key
    archive=directory/'reuse_before_binding_normalization';assert not archive.exists()
    archive.mkdir()
    refs={}
    for filename in ('result.json','notes.json','review.json','recipe.json','job.json'):
        source=directory/filename;target=archive/filename
        target.write_bytes(source.read_bytes());assert sha256(source)==sha256(target)
        refs[filename]=reference(target)
    evaluation['binding']=expected
    atomic_json(path,evaluation)
    notes['evaluation_sha256']=sha256(path);atomic_json(directory/'notes.json',notes)
    new_evaluation,new_items=get_items(path)
    assert new_items==items
    atomic_json(directory/'review.json',content_review(new_evaluation,sha256(path),notes,new_items))
    atomic_json(directory/'recipe.json',expected)
    job=read_json(directory/'job.json');job['binding']=expected;atomic_json(directory/'job.json',job)
    atomic_json(RUN/'parent_reuse_binding_normalization.json',dict(passed=True,completed_at=now(),
        source_sha256=sha256(Path(__file__)),config_sha256=c['config_sha256'],archived=refs,
        reason='Exact-binding assertion rejected provenance and historical extra fields inside binding',
        raw_outputs_and_actual_histories_unchanged=True,judgments_unchanged=True,
        provenance_retained_outside_binding=True,new_GPU_generation_seconds=0))
    print('Verified parent reuse binding normalized; raw/history/judgments unchanged; originals retained')


if __name__=='__main__':main()
