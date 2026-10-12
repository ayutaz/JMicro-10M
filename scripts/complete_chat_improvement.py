"""Audit bounded plan131 stages0-5 separately from model quality/adoption.

Requires actual final learning, all raw-bound reviews and fixed NLL. It never
marks conditional retention/sampling passed when no candidate is eligible.
"""
from datetime import datetime
import argparse
import json
import math
from pathlib import Path
import sys
import urllib.request
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.chat_review import content_review
from chat_improvement_contract import RUN,B,LIMITS,preflight,require_ref,reference
from phase6_performance import alive
from review_chat_improvement import get_items,fingerprint
from compare_chat_improvement import absolute_checks


def canonical(value):return json.loads(json.dumps(value))


def verify_review(path,config,ref,suite):
    evaluation,items=get_items(path);binding=evaluation['binding']
    assert binding['config_sha256']==config['config_sha256']
    assert binding['checkpoint_sha256']==ref['sha256']
    assert binding['source_sha256']==config['source_sha256']
    assert binding['suite_sha256']==config['new_DEV' if suite=='new' else 'old_suite']['sha256']
    assert binding['decoding']=='greedy' and binding['evaluation_seeds']==[42] and binding['evaluation_seed']==42
    assert binding['scored_split']=='dev' and binding['protected_test_used'] is False
    notes_path=path.with_name('notes.json');notes=read_json(notes_path)
    review=content_review(evaluation,sha256(path),notes,items)
    assert canonical(review)==read_json(path.with_name('review.json'))
    job=read_json(path.with_name('job.json'))
    assert job['status']=='complete' and job['binding']==binding
    if 'reuse_provenance' in job:
        provenance=job['reuse_provenance']
        assert provenance['new_GPU_generation_seconds']==0 and provenance['all219_raw_history_ID_bytes_verified']
        for key in ('original_evaluation','original_notes','original_job'):require_ref(provenance[key])
    else:assert not alive(job)
    if 'authored_score_file' in notes:require_ref(notes['authored_score_file'])
    current={r['key']:r for r in notes['judgments']}
    for row in notes['judgments']:
        reuse=row.get('reuse')
        if not reuse:continue
        if 'packet_key' in reuse:
            source=current[reuse['packet_key']]
            assert fingerprint(items[row['key']])==fingerprint(items[source['key']])==reuse['fingerprint']
        elif 'fingerprint' in reuse:
            note_ref=reuse['source_notes'];source_path=require_ref(note_ref)
            source_notes=read_json(source_path)
            source=next(r for r in source_notes['judgments'] if r['key']==note_ref['key'])
            source_evaluation,source_items=get_items(source_path.with_name('result.json'))
            content_review(source_evaluation,sha256(source_path.with_name('result.json')),source_notes,source_items)
            assert fingerprint(items[row['key']])==fingerprint(source_items[source['key']])==reuse['fingerprint']
        else:
            assert 'reuse_provenance' in evaluation
            note_ref=reuse['source_notes'];source_notes=read_json(require_ref(note_ref))
            source=next(r for r in source_notes['judgments'] if r['key']==reuse['original_key'])
        assert all(row[k]==source[k] for k in ('grammar','relevance','context','rationale'))
    return dict(raw=reference(path),notes=reference(notes_path),review=reference(path.with_name('review.json')),
        judgment_count=len(items),content=review['summaries'],mechanical={k:evaluation[k] for k in (
            'primary','role_control','own_history_final24','own_history_all_turns')},
        absolute_checks=absolute_checks(evaluation,review),dev_screen_passed=review['dev_screen_passed'],
        reused_historical_GPU_generation='reuse_provenance' in evaluation)


def verify_nll(path,config,ref,common):
    nll=read_json(path);binding=nll['binding']
    assert nll['status']=='complete' and binding['config_sha256']==config['config_sha256']
    assert binding['checkpoint']['sha256']==ref['sha256'] and binding['fixed_targets']==config['fixed_NLL']
    targets=nll['targets'];assert len(targets)==2554
    identities=[(r['id'],r['dataset'],r['body_teachers'],r['EOT_teachers'],r['body_bytes']) for r in targets]
    assert identities==common and len({r['id'] for r in targets})==2554
    assert nll['provided_gold_history'] and nll['own_generated_quality'] is False and nll['protected_TEST_used'] is False
    for row in targets:
        assert all(math.isfinite(row[k]) and row[k]>=0 for k in ('body_NLL','EOT_NLL'))
        assert row['body_teachers']>0 and row['EOT_teachers']==1 and row['body_bytes']>0
    for dataset,summary in nll['summaries'].items():
        rows=[r for r in targets if r['dataset']==dataset]
        assert len(rows)==summary['targets']
        for key in ('body_NLL','EOT_NLL','body_teachers','EOT_teachers','body_bytes'):
            assert math.isclose(sum(r[key] for r in rows),summary[key],rel_tol=1e-12,abs_tol=1e-10)
        assert math.isclose(summary['body_NLL']/summary['body_teachers'],summary['body_mean_NLL'],rel_tol=1e-12)
        assert math.isclose(summary['EOT_NLL']/summary['EOT_teachers'],summary['EOT_mean_NLL'],rel_tol=1e-12)
        assert math.isclose(summary['body_NLL']/summary['body_bytes']/math.log(2),summary['body_BPB'],rel_tol=1e-12)
    return dict(reference=reference(path),targets=len(targets),summaries=nll['summaries'])


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--intermediate',action='store_true');args=parser.parse_args()
    config,_,_=preflight(ROOT/'configs/phase7/chat-improvement-20261012.json')
    assert config['config_sha256']=='f18554e4ee8ed2c53ac41ae40d3b1f0db8d09c1cfe14ae47c2985676479169e3'
    for name,digest in config['source_sha256'].items():assert sha256(RUN/'source'/name)==digest,name
    if args.intermediate:
        refs={('parent','t0'):config['parent']}
        for arm in ('C0','C1'):refs[arm,'t1']=read_json(RUN/arm/'checkpoints.json')['t1']
        first=read_json(RUN/'NLL/parent/t0.json')['targets']
        common=[(r['id'],r['dataset'],r['body_teachers'],r['EOT_teachers'],r['body_bytes']) for r in first]
        reviews={};nlls={}
        for (arm,point),ref in refs.items():
            require_ref(ref)
            nlls[arm+'-'+point]=verify_nll(RUN/'NLL'/arm/(point+'.json'),config,ref,common)
            for suite in ('new','old'):
                reviews[arm+'-'+point+'-'+suite]=verify_review(RUN/'evaluation'/arm/point/suite/'greedy/result.json',config,ref,suite)
        atomic_json(RUN/'intermediate_review_audit.json',dict(passed=True,config_sha256=config['config_sha256'],
            source_sha256=sha256(Path(__file__)),completed_at=now(),reviews=reviews,fixed_NLL=nlls,
            judgment_count=6*219,scope_complete=False,requested_stages_0_to_5_complete=False,
            Base_adopted=False,Chat_adopted=False,model_quality_complete=False))
        print('Intermediate raw/history/judgment/NLL audit passed; full stages0-5 remain incomplete')
        return
    gates={}
    for filename in ('native_probe.json','native_resume_gate.json','evaluation_forecast.json'):
        report=read_json(RUN/filename)
        assert report['passed'] and report['config_sha256']==config['config_sha256']
        gates[filename]=reference(RUN/filename)
    training={};checkpoint_refs={('parent','t0'):config['parent']}
    for arm in ('C0','C1'):
        directory=RUN/arm;job=read_json(directory/'job.json');result=read_json(directory/'result.json')
        audit=read_json(directory/'training_audit.json')
        assert job['status']==result['status']=='learning_complete' and not alive(job)
        assert audit['passed'] and audit['config_sha256']==config['config_sha256']
        assert audit['Assistant_teachers']==B and audit['parameter_count']==10001152
        require_ref(audit['metrics'])
        points=read_json(directory/'checkpoints.json');assert points==result['checkpoints']
        assert set(points)=={'t1','t2','t3'} and audit['updates']==result['checkpoint']['update']
        for point,ref in points.items():
            require_ref(ref);assert ref==audit['checkpoints'][point]['reference']
            checkpoint_refs[arm,point]=ref
        training[arm]=dict(audit=reference(directory/'training_audit.json'),job=reference(directory/'job.json'),
            result=reference(directory/'result.json'),checkpoints=points,updates=audit['updates'],
            Assistant_teachers=B,padding_fraction=1-result['checkpoint']['valid_inputs']/result['checkpoint']['physical_inputs'])
    first=read_json(RUN/'NLL/parent/t0.json')['targets']
    common=[(r['id'],r['dataset'],r['body_teachers'],r['EOT_teachers'],r['body_bytes']) for r in first]
    evaluations={};nlls={}
    for (arm,point),ref in checkpoint_refs.items():
        nlls[arm+'-'+point]=verify_nll(RUN/'NLL'/arm/(point+'.json'),config,ref,common)
        for suite in ('new','old'):
            path=RUN/'evaluation'/arm/point/suite/'greedy/result.json'
            evaluations[arm+'-'+point+'-'+suite]=verify_review(path,config,ref,suite)
    assert len(evaluations)==14 and sum(r['judgment_count'] for r in evaluations.values())==3066
    selection=read_json(RUN/'selection.json')
    assert selection['config_sha256']==config['config_sha256'] and selection['point']=='t3'
    for arm in ('C0','C1'):
        for suite in ('new','old'):
            actual=evaluations[arm+'-t3-'+suite]
            selected=selection['summary'][arm][suite]
            assert selected['absolute_checks']==actual['absolute_checks']
            assert selected['content']==actual['content'] and selected['mechanical']==actual['mechanical']
    if selection['eligible_candidate'] is not None:
        raise RuntimeError('Eligible candidate: actual retention and all three-seed content reviews required before completion')
    assert not selection['both_suites_passed'] and not any(selection['eligibility'].values())
    data=read_json(RUN/'GPU_ledger.json');totals={k:0. for k in LIMITS};previous_end=None
    for row in data['entries']:
        assert row['status'] in ('complete','failed_or_stopped') and not alive(row)
        assert row['config_sha256']==config['config_sha256']
        start=datetime.fromisoformat(row['started_at']);end=datetime.fromisoformat(row['ended_at'])
        assert start<=end and (previous_end is None or previous_end<=start)
        assert 0<row['charged_seconds']<=(end-start).total_seconds()+2
        totals[row['category']]+=row['charged_seconds'];previous_end=end
    assert all(totals[k]<=LIMITS[k] for k in LIMITS) and sum(totals.values())<=21600
    assert math.isclose(sum(totals.values()),data['total_charged_seconds'],abs_tol=1e-8)
    ui=read_json(ROOT/'reports/local/webui/server.json');assert ui['status']=='running' and alive(ui)
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response:http=json.load(response)
    assert http['checkpoint_sha256']==config['parent']['sha256'] and not http['busy']
    # The original idle UI may hold the shared lock. Verify current ownership;
    # no experiment process is allowed to remain after stages0-5.
    import check_chat_improvement_launch
    check_chat_improvement_launch.main()
    result=dict(status='bounded_comparison_complete_no_candidate',requested_stages_0_to_5_complete=True,
        completed_at=now(),source_sha256=sha256(Path(__file__)),config=reference(Path(config['config_path'])),
        stages=dict(stage0='frozen_and_preserved',stage1='TRAIN_DEV_prepared_and_reviewed',
            stage2='native_finite_and_exact_resume_passed',stage3='both_full_B_learned',
            stage4='all14_greedy_reviews_and7_fixed_NLL_complete_no_candidate',stage5='audited_report_and_stop'),
        training=training,evaluations=evaluations,fixed_NLL=nlls,gates=gates,
        selection=reference(RUN/'selection.json'),GPU_ledger=reference(RUN/'GPU_ledger.json'),
        GPU_seconds_by_category=totals,GPU_total_seconds=sum(totals.values()),GPU_limit_seconds=21600,
        raw_metadata_judgments=3066,new_GPU_greedy_outputs=2847,reused_parent_old_outputs=219,
        fixed_NLL_target_evaluations=7*2554,
        conditional_retention=dict(status='skipped_no_eligible_candidate',passed=False,quality_unconfirmed=True),
        conditional_sampling=dict(status='skipped_no_eligible_candidate',passed=False,quality_unconfirmed=True),
        scope_complete=True,Base_adopted=False,Chat_adopted=False,model_quality_complete=False,
        independent_trained_seed=False,independent_human_blind=False,fullDEV=False,protected_TEST_used=False,
        efficiency_comparison_executed=False,C2_recovery_executed=False,quantization_executed=False,
        public_publication_executed=False,original_UI=dict(observed_at=now(),identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},HTTP=http),
        caveats=['Codex nonblind exploratory ratings','New own24 overlaps provided80',
            'Saved points are repeated families, not extra independent cases','TRAIN low NLL is not generalization',
            'No claim that 10M capacity limit is established','Historical reuse is not new independent GPU evidence'])
    atomic_json(RUN/'completion.json',result)
    print('Actual stages0-5 comparison audit passed; no candidate; Base/Chat remain unadopted')


if __name__=='__main__':main()
