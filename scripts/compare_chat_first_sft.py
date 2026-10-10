"""Fixed DEV checkpoint selection and family-paired diagnostic comparisons."""
import argparse
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,write_json,now
from jmicro.chat_review import paired_chat_comparison
from review_chat_first_sft import load_evaluation
from chat_first_contract import RUN


def select_checkpoint(rows, baseline_repetition):
    eligible=[r for r in rows if r['dev_screen_passed'] and r['repetition']<=baseline_repetition]
    # Preserve a failed diagnostic best for illustration, never call it eligible.
    order=lambda r:(r['joint'],r['context'],-r['repetition'],-r['epoch'])
    return (max(eligible,key=order) if eligible else None),max(rows,key=order)


def comparison(base_dir, candidate_dir):
    base,base_items=load_evaluation(base_dir/'result.json')
    target,target_items=load_evaluation(candidate_dir/'result.json')
    a,b=read_json(base_dir/'content_review.json'),read_json(candidate_dir/'content_review.json')
    for ev,review,directory in ((base,a,base_dir),(target,b,candidate_dir)):
        assert review['evaluation_sha256']==sha256(directory/'result.json')
        assert review['checkpoint_sha256']==ev['binding']['checkpoint_sha256']
    report=paired_chat_comparison(base,target,base_items,target_items,a,b)
    report['difference_direction']='SFT candidate minus unadopted original10B Base; positive failure differences mean regression'
    report['summaries']=dict(base=a['summaries'],candidate=b['summaries'])
    report['dev_screens']=dict(base=a['dev_screen_passed'],candidate=b['dev_screen_passed'])
    report['status']='matched_chat_first_dev_comparison_only'
    report['Base_adopted']=False
    report['evidence']=dict(base=dict(evaluation_sha256=sha256(base_dir/'result.json'),review_sha256=sha256(base_dir/'content_review.json')),
        candidate=dict(evaluation_sha256=sha256(candidate_dir/'result.json'),review_sha256=sha256(candidate_dir/'content_review.json')))
    return report,target,b


def run():
    base_dir=RUN.with_name(RUN.name+'-base-chat')/'greedy'
    baseline=read_json(base_dir/'result.json');rows=[];comparisons={}
    for n in (1,2,3):
        directory=RUN.with_name(RUN.name+f'-epoch{n}-chat')/'greedy'
        report,ev,review=comparison(base_dir,directory);comparisons[f'epoch{n}']=report
        rows.append(dict(epoch=n,dev_screen_passed=review['dev_screen_passed'],
            joint=review['summaries']['primary']['joint_grammar_relevance_score2'],
            context=review['summaries']['own_history_final24']['context_score2'],repetition=ev['primary']['repetition'],
            checkpoint=ev['binding']['diagnostic_provenance']['checkpoint'],review_path=str(directory/'content_review.json')))
    selected,best=select_checkpoint(rows,baseline['primary']['repetition'])
    out=dict(status='all_four_greedy_conditions_reviewed',fixed_rule='DEV screen; no repetition increase; joint, context, fewer repeats, earlier checkpoint',
        comparisons=comparisons,checkpoint_summaries=rows,selected_candidate=selected,diagnostic_best=best,
        sampling_required=selected is not None,retention_required=selected is not None,
        independent_human_blind=False,protected_test_used=False,Base_adopted=False,Chat_adopted=False,
        created_at=now(),statistical_note='DEV-selected checkpoints; descriptive paired bootstrap, not independent confirmation')
    write_json(RUN/'greedy_comparison.json',out)
    print('Fixed DEV selection:',None if selected is None else selected['epoch'],'; diagnostic best:',best['epoch'])


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);argparse.ArgumentParser().parse_args();run()
