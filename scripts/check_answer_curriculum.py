"""CPU scope, actual fixture coverage and frozen-adapter checks before CUDA."""
import json
from pathlib import Path
import tempfile
from unittest.mock import patch
from answer_learning_common import ROOT,RUN as PARENT_RUN,save,ref,read_json,now,sha256
import answer_curriculum_contract as contract
import run_answer_curriculum as runner


def main():
    target=PARENT_RUN/'curriculum_CPU_checks.json';assert not target.exists()
    c,tok,arms=contract.preflight();checks={}
    before={p:sha256(ROOT/p) for p in ('scripts/run_chat_natural.py','scripts/evaluate_chat_natural.py','scripts/chat_natural_contract.py')}
    runner.wire_reuse()
    checks['training_and_evaluation_new_paths']=runner.native.RUN==runner.evaluation.RUN==contract.RUN and runner.native.DATA==contract.DATA
    checks['same_native_trainer']=runner.native.TeacherChatTrainer.__module__=='jmicro.teacher_chat_training'
    checks['new_common_LR_and_teacher_budget']=runner.native.SPEC['lr']==1e-4 and runner.native.BUDGET==1000000
    checks['all6_suites_including_previous_new']=tuple(runner.evaluation.SUITES)==contract.SUITES and len(contract.SUITES)==6
    for arm,rows in arms.items():
        fixture=runner.fixture(rows,arm);checks[arm+'_fixture48_unique']=len(fixture)==len({r['doc_id'] for r in fixture})==48
        if arm=='C1':
            checks['candidate_actual_all8_authored_families']=len({r.get('family') for r in fixture if r['source']=='Authored_grounded_TRAIN'})==8
            checks['candidate_actual_both_reviewed_sources']=all(sum(r['source']==s for r in fixture)==4 for s in ('Dolly_llmjp','Aya_Japanese_TRAIN'))
    nll=runner.windows(c,tok)
    checks['all320_complete_NLL_targets']=len(nll)==320 and all((y!=-100).sum()>=2 for _,_,y in nll)
    checks['distinct_old_new_DEV_NLL_labels']=sum(r['dataset']=='previous_new_DEV' for r,_,_ in nll)==80 and sum(r['dataset']=='new_DEV' for r,_,_ in nll)==80
    checks['supplement32_NLL_targets']=sum(r['dataset']=='supplement_TRAIN' for r,_,_ in nll)==32
    checks['NLL_unique_IDs']=len({r['id'] for r,_,_ in nll})==320
    for label,path in dict(TEST=contract.DATA/'TEST.jsonl',train=contract.DATA/'C0_TRAIN.jsonl',mixed=contract.DATA/'dev_suites/mixed.jsonl',
        sibling=contract.DATA.parent/'dev_suites/new.jsonl').items():
        with patch.object(contract,'bound',side_effect=RuntimeError('Forbidden file was opened')):
            try:contract.read_dev(dict(path=str(path),sha256='0'*64))
            except AssertionError:checks['reject_'+label+'_before_open']=True
            else:raise AssertionError(label)
    contract.RUN.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(dir=contract.RUN,prefix='CPU-fixture-') as temp:
        base=Path(temp);(base/'dev_suites').mkdir();destination=base/'dev_suites/new.jsonl'
        valid,_=contract.read_dev(c['suites']['new'])
        for label,altered in [('subset',valid[:-1]),('duplicate_family',valid[:-1]+[valid[0]]),
            ('TEST_split',[dict(valid[0],split='test')]+valid[1:]),('train_split',[dict(valid[0],split='train')]+valid[1:])]:
            destination.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in altered))
            with patch.object(contract,'DATA',base):
                try:contract.read_dev(ref(destination))
                except AssertionError:checks['reject_actual_'+label]=True
                else:raise AssertionError(label)
    checks['old_sources_unchanged']={p:sha256(ROOT/p) for p in before}==before
    assert all(checks.values()),checks
    save(target,dict(status='passed',created_at=now(),checks=checks,total=len(checks),config=ref(contract.CONFIG),
        source=ref(__file__),old_sources=before,no_model_forward=True,new_GPU_updates=0,new_TEST_body_read=False,
        role='Admission/scope/adapters only, not quality evidence'))
    print('CPU checks passed: '+str(len(checks)))


if __name__=='__main__':main()
