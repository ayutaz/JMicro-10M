"""Requirement-by-requirement five-step completion, distinct from model adoption."""
import json
from two_attribute_contract import RUN,CONFIG,preflight
from answer_learning_common import save,ref,bound,read_json,now
from phase6_performance import alive
from review_two_attribute_diagnosis import items
from review_two_attribute_regression import wire,public_validate
import review_chat_natural as review

def main():
    c,_,rows=preflight();target=RUN/'completion.json';assert not target.exists()
    manifest=read_json(bound(c['TRAIN_manifest']));qa=read_json(bound(c['TRAIN_review']));learning=read_json(RUN/'learning_audit.json')
    gate=read_json(RUN/'native_gate.json');diagnosis=read_json(RUN/'diagnosis/notes.json');analysis=read_json(RUN/'final_analysis.json')
    assert len(rows)==64 and qa['all64_directly_read'] and len(qa['judgments'])==64 and manifest['review']==c['TRAIN_review']
    assert learning['config']==ref(CONFIG) and all(learning['checks'].values()) and gate['config_sha256']==c['config_sha256'] and gate['passed'] and all(gate['resume_checks'].values())
    assert len(gate['all32_timings'])==32 and len(items())==len(diagnosis['judgments'])==240
    assert diagnosis['config']==ref(CONFIG) and analysis['config']==ref(CONFIG) and analysis['judgments']==1973
    assert analysis['branch'] in ('investigate_TRAIN_fit_before_main_SFT','investigate_transfer_before_main_SFT','prepare_new_matched_main_SFT')
    assert not analysis['Chat_adopted'] and not analysis['Base_adopted'] and not analysis['new_TEST']
    if analysis['branch']=='prepare_new_matched_main_SFT':
        raise AssertionError('Readiness reached: separately prepare matched main contract and complete required conditional work before claiming all five steps')
    wire();count=0
    for suite in c['suites']:
        path=RUN/'evaluation/D'/suite/'result.json';raw,view,objects=review.get_items(path);notes=read_json(path.with_name('notes.json'))
        verified=review.content_review(view,ref(path)['sha256'],notes,objects);assert json.loads(json.dumps(verified))==read_json(path.with_name('review.json'));count+=len(notes['judgments'])
    path,raw,_=public_validate('D');n=read_json(path.with_name('notes.json'));assert n['raw']==ref(path) and len(n['judgments'])==200;count+=200
    assert count==1733;bound(analysis['export'])
    job=read_json(RUN/'pipeline.json');assert job['status']=='complete_raw_pending_review' and not alive(job)
    terminal=read_json(RUN/'terminal_observation.json');assert terminal['pipeline']==ref(RUN/'pipeline.json') and not terminal['actual_alive']
    assert alive(terminal['actual_identity']) and terminal['restored_UI']['checkpoint_sha256']==c['parent']['sha256']
    windows=read_json(RUN/'windows_terminal_observation.json');assert windows['matching_worker_absent'] and windows['launcher_result']['status']=='complete_raw_pending_review'
    assert windows['launcher_result']['exit_code']==windows['launcher_result']['original_UI_restore_exit_code']==0
    ledger=read_json(RUN/'GPU_ledger.json');assert all(r['status']=='complete' for r in ledger['entries'])
    for category,limit in c['limits_seconds'].items():assert sum(r['seconds'] for r in ledger['entries'] if r['category']==category)<=limit
    save(target,dict(created_at=now(),config=ref(CONFIG),source=ref(__file__),status='all_five_steps_completed_candidate_not_adopted',
        requirements={
            '1_TRAIN64_authored_and_all_verified':dict(passed=True,manifest=c['TRAIN_manifest'],review=c['TRAIN_review']),
            '2_small_SFT_original_Base_fresh_Adam':dict(passed=True,gate=ref(RUN/'native_gate.json'),audit=ref(RUN/'learning_audit.json')),
            '3_unseen64_and_actual_own16_all240':dict(passed=True,notes=ref(RUN/'diagnosis/notes.json')),
            '4_result_based_branch_and_closed_condition':dict(passed=True,decision=analysis['branch'],evidence=ref(RUN/'final_analysis.json'),main_SFT_started=False),
            '5_all_existing7_and_public100_regressions':dict(passed=True,responses=1733,analysis=ref(RUN/'final_analysis.json'))},
        all1973_reviews=True,total_GPU_stage_seconds=ledger['total_seconds'],previous_GPU_ledger=c['previous_GPU_ledger'],
        scientific_process_terminal=ref(RUN/'terminal_observation.json'),windows_worker_terminal=ref(RUN/'windows_terminal_observation.json'),
        original_UI_restored=True,Chat_adopted=False,Base_adopted=False,new_TEST=False,
        stable_chat_model_completed=False,formal_Base_and_independent_whole_pipeline_completed=False))
    print('Five steps verified; experimental completion does not certify model quality')

if __name__=='__main__':main()
