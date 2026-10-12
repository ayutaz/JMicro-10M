"""Reuse only verified original-parent/old-suite raw results and judgments."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.chat_review import review_items,content_review
from chat_improvement_contract import RUN,preflight,reference,require_ref
from evaluate_chat_improvement import load_cases
from phase6_performance import alive


def main():
    c,tok,_=preflight(ROOT/'configs/phase7/chat-improvement-20261012.json')
    old=ROOT/'reports/phase7/chat-first-sft-20261010-base-chat/greedy'
    evaluation=read_json(old/'result.json');notes=read_json(old/'content_notes.json');job=read_json(old/'job.json')
    assert job['status']=='complete' and not alive(job)
    b=evaluation['binding'];require_ref(c['parent']);require_ref(c['tokenizer']);require_ref(c['old_suite'])
    assert b['checkpoint_sha256']==c['parent']['sha256'] and b['tokenizer_sha256']==c['tokenizer']['sha256']
    assert b['suite_sha256']==c['old_suite']['sha256'] and b['implementation']==c['implementation']
    assert b['max_new_tokens']==64 and b['model_context']==1024 and b['dtype']=='bf16' and b['backend']=='math'
    assert b['decoding']=='greedy' and b['evaluation_seed']==42 and b['evaluation_seeds']==[42]
    core=('src/jmicro/chat_evaluation.py','src/jmicro/tokenizer.py','src/jmicro/japanese_evaluation.py')
    for source in core:
        assert b['source_sha256'][source]==c['source_sha256'][source]==sha256(ROOT/source)
        assert sha256(old/'source'/source)==sha256(ROOT/source)
    cases,_=load_cases(c['old_suite']['path'],tok);items=review_items(evaluation,cases,tok,1024)
    review=content_review(evaluation,sha256(old/'result.json'),notes,items)
    destination=RUN/'evaluation/parent/t0/old/greedy';assert not (destination/'result.json').exists()
    provenance=dict(kind='verified_prior_identical_parent_suite_generation_core',original_evaluation=reference(old/'result.json'),
        original_notes=reference(old/'content_notes.json'),original_job=reference(old/'job.json'),
        original_binding=b,core_source_SHA_identical=True,all219_raw_history_ID_bytes_verified=True,reused_at=now(),
        new_GPU_generation_seconds=0,not_new_independent_evidence=True)
    binding=dict(b,config_sha256=c['config_sha256'],stage='parent-t0',source_sha256=c['source_sha256'],reuse_provenance=provenance)
    evaluation=dict(evaluation,binding=binding,reuse_provenance=provenance)
    atomic_json(destination/'result.json',evaluation)
    new_notes=dict(notes,evaluation_sha256=sha256(destination/'result.json'),
        reviewer=dict(kind='codex_nonblind',identity='Codex plan131 reviewer',independent_human=False,blind=False),
        reuse_provenance=provenance)
    for row in new_notes['judgments']:row['reuse']=dict(source_notes=provenance['original_notes'],original_key=row['key'])
    atomic_json(destination/'notes.json',new_notes)
    new_items=review_items(evaluation,cases,tok,1024)
    atomic_json(destination/'review.json',content_review(evaluation,sha256(destination/'result.json'),new_notes,new_items))
    atomic_json(destination/'recipe.json',binding)
    atomic_json(destination/'job.json',dict(status='complete',binding=binding,reuse_provenance=provenance,completed_at=now(),GPU_elapsed_seconds=0))
    atomic_json(RUN/'parent_old_reuse.json',provenance)
    print('Verified prior original-parent old-suite raw219 judgments retained; no GPU generation repeated')

if __name__=='__main__':main()
