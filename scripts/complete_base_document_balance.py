"""Close one rejected study with explicit qualified-only decisions and preservation."""
import hashlib
import json
from pathlib import Path
import re
import sys
from datetime import datetime, timezone
from urllib.request import urlopen

ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/'reports/phase6/base-document-balance-comparison-20261014'
OUTPUT=ROOT/'reports/phase6/base_document_balance_comparison_completion.json'
sys.path.insert(0,str(Path(__file__).resolve().parent))
from observe_base_document_balance import live


def read(path): return json.loads(path.read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def ref(path): return dict(path=str(path.relative_to(ROOT)),sha256=sha(path))


def main():
    if OUTPUT.exists(): raise ValueError('Preserve completed condition; no second closeout')
    plan=read(ROOT/'configs/phase6/base_document_balance_comparison.json')
    review=read(ROOT/'reports/phase6/base_document_balance_comparison_review.json')
    numeric=read(RUN/'numeric_completion_audit.json')
    job=read(RUN/'job.json')
    result=read(RUN/'result.json')
    assert job['status']==result['status']=='complete' and not live(job)
    assert numeric['passed'] and numeric['history']['all_committed_updates']==17698
    assert numeric['history']['actual_original_teacher_positions']==100000000
    assert numeric['full_checkpoint_sha256']==result['training']['checkpoint_sha256']
    assert review['result_sha256']==sha(RUN/'result.json')
    assert review['config_sha256']==sha(ROOT/'configs/phase6/base_document_balance_comparison.json')
    assert review['all80_individually_read'] and not review['independent_human_blind']
    assert review['eligible_for_final_Base_validation'] is False
    assert review['matched_objective_quality']['passed'] is False
    assert review['quality_comparison']['passed'] is False
    assert not all(review['absolute_dev_screen'].values()) and not all(review['original_Web'].values())
    notes=ROOT/'reports/phase6/base_document_balance_notes.json'
    assert review['notes_sha256']==sha(notes)
    cases=read(notes)['notes']
    assert len(cases)==80 and len({r[0] for r in cases})==80 and all(len(r[5].strip())>=12 for r in cases)
    assert review['summaries']['document_balance']['coherent']==sum(r[3]==2 for r in cases)
    assert review['summaries']['document_balance']['appropriate']==sum(r[4] for r in cases)
    for path,digest in plan['source_sha256'].items(): assert sha(ROOT/path)==digest,path
    assert sha(ROOT/'src/jmicro/model.py')=='298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83'
    assert plan['goals']==dict(web=75000000,textbook=20000000,story=5000000)
    # Count split declarations without JSON-parsing, displaying or selecting
    # TEST bodies. The frozen generator already parsed them before filtering.
    suite=ROOT/'eval/base.jsonl'
    raw=suite.read_bytes()
    assert sha(suite)==plan['suite_sha256']
    counts={split:len(re.findall(rb'"split"\s*:\s*"'+split.encode()+rb'"',raw)) for split in ('dev','test')}
    assert counts==dict(dev=80,test=20)
    incident=dict(recorded_at=datetime.now(timezone.utc).isoformat(),
        status='original_Base_TEST_prompt_CPU_parsing_exposure_confirmed_from_executed_frozen_reader',
        suite=ref(suite), unique_original_TEST_prompt_rows=counts['test'],
        generator_source=ref(ROOT/'scripts/run_eos_short_pilot.py'),
        review_reader_source=ref(ROOT/'scripts/review_parameter_displacement_anchor.py'),
        evidence='greedy80 JSON-parses every mixed-suite line before filtering split=dev; content reader does likewise. The completed generation80 and content review used these frozen sources.',
        execution_result=ref(RUN/'result.json'),raw_generation=ref(RUN/'evaluation/document_balance/evaluation/generation.json'),
        selected_generated_rows=80,selected_generated_split='dev',
        TEST_used_for_learning=False,TEST_used_for_GPU_scoring=False,
        original_TEST_prompts_can_be_called_unread=False,original_TEST_shards_opened=False,
        new_sealed_Base_TEST_required_if_qualified=True,CPU_parse_event_count_not_measured=True,
        previous_results_not_rewritten=True,
        correction='Old protected_test_used/scored=false proves lack of GPU test scoring here; it does not prove that the mixed TEST prompts were unopened on CPU. Keep this exposure explicit. Do not use or create replacement TEST while no eligible Base exists.')
    atomic=lambda path,value: path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n')
    incident_path=RUN/'original_TEST_prompt_exposure.json'
    if incident_path.exists(): raise ValueError('Preserve exposure correction')
    atomic(incident_path,incident)
    ui_record=read(ROOT/'reports/local/webui/server.json')
    assert live(ui_record)
    with urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response: ui=json.load(response)
    assert ui['parameters']==10001152 and ui['checkpoint_sha256']==plan['parent']['sha256']
    assert ui['tokenizer_sha256']==plan['tokenizer_sha256'] and ui['busy'] is False
    def skipped(reason): return dict(executed=False,passed=False,quality_unconfirmed=True,
        status='not_executed_no_eligible_candidate',reason=reason)
    branches=dict(main_comparison=skipped('Pilot full quality and all retention conditions failed.'),
        independent_fresh_trained_seed43=skipped('No qualified recipe; no source seed42 parent or generation RNG used as a substitute.'),
        fullDEV_and_400_plus40=skipped('No qualified two independently trained Base seeds.'),
        sealed_TEST=skipped('No qualified recipe or final seal; original TEST prompt CPU exposure requires fresh sealed cases if a future recipe qualifies.'),
        adoption=skipped('Original quality gates failed; Base remains unfinished and unadopted.'))
    completion=dict(status='document_balance100M_rejected_all80_and_conditional_decisions_closed',
        created_at=datetime.now(timezone.utc).isoformat(),
        result=ref(RUN/'result.json'),review=ref(ROOT/'reports/phase6/base_document_balance_comparison_review.json'),
        numeric_audit=ref(RUN/'numeric_completion_audit.json'),TEST_prompt_exposure=ref(incident_path),
        proposal=ref(ROOT/'reports/phase6/base_document_balance_proposal.json'),
        length_diagnostic=ref(ROOT/'reports/phase6/base_document_balance_length_diagnostic.json'),
        CPU_tests=[ref(ROOT/'reports/phase6/base_document_balance_CPU_tests.xml'),ref(ROOT/'reports/phase6/base_document_balance_run_tests.xml')],
        actual_updates=17698,new_scientific_original_teacher_positions=100000000,
        reused_control_original_teacher_positions=100000000,new_unique_dataset_tokens=0,
        new_GPU_seconds=result['GPU_occupancy_seconds'],probe_GPU_seconds=plan['probe_GPU_seconds'],
        total_new_GPU_seconds=result['GPU_occupancy_seconds']+plan['probe_GPU_seconds'],
        frozen_total_GPU_cap_seconds=4800,actual_study_GPU_cap_seconds=3855,
        native_parameters=10001152,all80_new_individually_read=True,
        independent_human_blind=False,summaries=review['summaries'],
        matched=review['matched_objective_quality'],strong=review['quality_comparison'],
        absolute=review['absolute_dev_screen'],historical_Web=review['original_Web'],
        qualified_only_branches=branches,fixed_condition_closed=True,
        comparison_and_required_conditional_decisions_complete=True,
        all_six_stages_actually_executed=False,requested_quality_end_state_achieved=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        TEST_prompt_CPU_exposure=True,TEST_scored=False,quality_criteria_unchanged=True,
        restored_UI_identity={k:ui_record[k] for k in ('pid','boot_id','start_ticks')},restored_UI=ui,
        scientific_process_exited=True,
        next_action='Report the rejected single comparison and stop at the agreed failure boundary. No coefficient/seed/parent/budget rescue, unrelated training, Chat, quantization or automatic publication.',
        limitations='Single mature-parent trained seed42, cached control, repeated nonblind DEV; no global corpus audit, no independent fresh Base seed, no fullDEV/finalTEST/adoption. This is neither proof of the sole cause nor proof that every document weighting objective fails.')
    atomic(OUTPUT,completion)
    print(json.dumps(dict(status=completion['status'],fixed_condition_closed=True,conditional_decisions=branches,
        Base_adopted=False,total_GPU_seconds=completion['total_new_GPU_seconds'],restored_UI=completion['restored_UI_identity']),ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
