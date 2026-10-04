from pathlib import Path
import sys
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from evaluate_complete_text_full import selected_candidate,parent_results

def test_conditional_evaluation_requires_verified_single_candidate():
    review={'status':'passed','checks':{'actual_GPU':True},'candidate_checks':{
        'short20':{'eligible_for_conditional_full':False},'coherent20':{'eligible_for_conditional_full':True}}}
    assert selected_candidate(review)=='coherent20'
    review['checks']['actual_GPU']=False
    with pytest.raises(AssertionError):selected_candidate(review)
    review['checks']['actual_GPU']=True
    review['candidate_checks']['coherent20']['eligible_for_conditional_full']=False
    with pytest.raises(AssertionError):selected_candidate(review)
    review['candidate_checks']['coherent20']['eligible_for_conditional_full']=True
    review['candidate_checks']['short20']['eligible_for_conditional_full']=True
    with pytest.raises(AssertionError):selected_candidate(review)

def test_parent_saved_results_accept_serialized_paths(tmp_path):
    body=tmp_path/'body.json';generation=tmp_path/'generation.json'
    body.write_text('{"body":{"bpb":0.95}}')
    generation.write_text('{"generation":{"outputs":[]}}')
    config={'parent_body':{'path':str(body)},'parent_generation':{'path':str(generation)}}
    assert parent_results(config)==({'bpb':.95},{'outputs':[]})
