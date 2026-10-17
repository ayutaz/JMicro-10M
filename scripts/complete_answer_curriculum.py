"""Requirement-by-requirement closure of plan151; no training or quality adoption."""
import json
import os
from pathlib import Path
from urllib.request import urlopen
import torch
from answer_learning_common import ROOT,RUN as PARENT_RUN,save,ref,bound,read_json,now
from run_answer_curriculum_resource_v2 import CONFIG,RUN,contract
from phase6_performance import alive,identity,finite_state
from jmicro.phase5 import equal_state
from review_answer_curriculum import wire,historical_index
import review_chat_natural as reviewer
from jmicro.chat_review import content_review


def main():
    target=RUN/'completion.json';assert not target.exists(),'Keep completed evidence immutable'
    c,tok,_=contract.preflight(load_records=False);wire();historical=historical_index()
    final=read_json(RUN/'final_analysis.json');assert final['config']==ref(CONFIG) and final['judgments']==2628
    job=read_json(RUN/'pipeline.json')
    assert job['status']=='complete_raw_pending_all_content_and_UI' and not alive(job)
    assert read_json(RUN/'evaluation_raw_complete.json')['responses']==2628
    reference=read_json(PARENT_RUN/'reference_notes.json');bound(reference['raw']);bound(reference['authored'])
    assert reference['status']=='all80_content_reviewed' and sum(len(v) for v in reference['judgments'].values())==80
    audit=read_json(PARENT_RUN/'TRAIN_capability_review.json');bound(audit['sample']);bound(audit['authored'])
    assert len(audit['judgments'])==120
    diagnosis=read_json(PARENT_RUN/'diagnostic-manifest-v2/completion.json')
    assert diagnosis['passed'] and diagnosis['status']=='all32_TRAIN_memorization_diagnosis_complete'
    for name in ('checkpoint','authored','before','after'):bound(diagnosis[name])
    assert len(diagnosis['judgments']['before'])==len(diagnosis['judgments']['after'])==32
    for source in ('dolly','aya'):
        qa=read_json(PARENT_RUN/f'{source}_QA_review.json');bound(qa['sample']);bound(qa['authored']);assert len(qa['judgments'])==120
    variants=read_json(PARENT_RUN/'curriculum_variant_QA_review.json')
    assert len(variants['judgments'])==32 and all(row['accepted'] for row in variants['judgments'])
    bound(variants['sample']);bound(variants['inventory']);bound(variants['authored_review_source'])
    gate=read_json(RUN/'native_gate.json');assert gate['passed'] and gate['config_sha256']==ref(CONFIG)['sha256'] and gate['technical_updates']==40
    gate_fields={}
    for arm in ('C0','C1'):
        proof=gate['arms'][arm];assert len(proof['all16_timing_updates'])==16 and all(proof['resume_all_fields'].values())
        left=torch.load(bound(proof['snapshots']['continuous']),map_location='cpu',weights_only=False)
        right=torch.load(bound(proof['snapshots']['resumed']),map_location='cpu',weights_only=False)
        assert set(left)==set(right) and finite_state(left) and finite_state(right)
        checks={key:equal_state(left[key],right[key]) for key in left};assert all(checks.values())
        gate_fields[arm]=checks;del left,right
    training={};practical={};manual=reused=0
    for arm in ('C0','C1'):
        training[arm]=read_json(RUN/arm/'training_audit.json')
        assert training[arm]['passed'] and training[arm]['config']==ref(CONFIG)
        bound(training[arm]['checkpoint']);bound(training[arm]['metrics'])
        expected=read_json(bound(c['arms'][arm]['dry_run']))
        assert training[arm]['updates']==expected['updates'] and training[arm]['Assistant_teachers']==expected['actual_teachers']
        for point in ('250000','500000'):
            notes=read_json(RUN/'diagnostics'/arm/f'{point}_notes.json')
            bound(notes['raw']);authored=read_json(bound(notes['authored']))
            assert notes['all10_reviewed'] and len(notes['judgments'])==len(authored)==10
            assert authored==[[row[k] for k in ('grammar','relevance','context','rationale')] for row in notes['judgments']]
        for suite in contract.SUITES:
            path=RUN/'evaluation'/arm/suite/'result.json';raw,view,items=reviewer.get_items(path)
            notes=read_json(path.with_name('notes.json'));review=content_review(view,ref(path)['sha256'],notes,items)
            assert json.loads(json.dumps(review))==read_json(path.with_name('review.json'))
            assert len(notes['judgments'])==219
            ratings={note['key']:note for note in notes['judgments']}
            for note in notes['judgments']:
                if 'reuse' not in note:continue
                reuse=note['reuse'];fp=reviewer.fingerprint(items[note['key']]);assert fp==reuse['fingerprint']
                if 'same_packet_key' in reuse:
                    prior=ratings[reuse['same_packet_key']]
                    assert reviewer.fingerprint(items[prior['key']])==fp
                else:
                    source=read_json(bound(reuse['source_notes']))
                    prior=next(n for n in source['judgments'] if n['key']==reuse['source_notes']['key'])
                    old_root=ROOT/'reports/phase7/chat-natural-sft-20261017/evaluation'
                    if Path(reuse['source_notes']['path']).is_relative_to(old_root):
                        assert fp in historical and all(note[k]==historical[fp][k] for k in ('grammar','relevance','context'))
                assert all(note[k]==prior[k] for k in ('grammar','relevance','context','rationale'))
            packet=read_json(path.with_name('packet.json'));assert packet['evaluation_sha256']==ref(path)['sha256']
            manual+=len(packet['pending']);reused+=len(packet['reused'])
            for name in ('raw','notes','review'):bound(final['summaries'][suite][arm][name])
        raw_path=RUN/'practical'/arm/'raw.json';raw=read_json(raw_path);notes=read_json(raw_path.with_name('notes.json'))
        assert raw['status']=='all10_actual_responses_saved_pending_content_notes'
        assert len(raw['conversations'])==5 and sum(len(v['turns']) for v in raw['conversations'])==10
        assert notes['all10_reviewed'] and notes['raw']==ref(raw_path) and len(notes['judgments'])==10
        authored=read_json(bound(notes['authored']))
        assert authored==[[row[k] for k in ('grammar','relevance','context','rationale')] for row in notes['judgments']]
        ui=read_json(raw_path.with_name('UI_observation.json'));assert ui['response_choices']==[16,32,64] and ui['default_tokens']==32
        practical[arm]=dict(raw=ref(raw_path),notes=ref(raw_path.with_name('notes.json')),UI=ref(raw_path.with_name('UI_observation.json')))
    assert manual+reused==2628
    for arm,points in final['NLL'].items():
        for point in points.values():
            values=read_json(bound(point['source']));assert len(values['targets'])==320
    if final['candidate_improvement_demonstrated']:
        reproduction=read_json(RUN/'seed43_reproduction.json')
        assert reproduction['complete'] and reproduction['seed']==43 and reproduction['prospective_contract']
        bound(reproduction['prospective_contract']);bound(reproduction['analysis'])
        conditional_seed=ref(RUN/'seed43_reproduction.json')
    else:conditional_seed='Not triggered: prospective criterion of positive new-content CI and no known-suite count regression did not hold'
    ledger=read_json(RUN/'GPU_ledger.json');assert len(ledger['entries'])==5
    assert ledger['entries'][0]['status']=='failed_or_interrupted' and ledger['entries'][0]['seconds']==c['inherited_probe_seconds']
    assert all(row['status']=='complete' for row in ledger['entries'][1:])
    for category,cap in c['limits_seconds'].items():assert sum(row['seconds'] for row in ledger['entries'] if row['category']==category)<=cap
    assert abs(ledger['total_seconds']-sum(row['seconds'] for row in ledger['entries']))<1e-8
    windows=read_json(RUN/'windows_terminal_observation.json')
    assert not windows['process_present'] and windows['launcher_result']['status']=='complete_raw_pending_content_and_UI'
    assert windows['launcher_result']['exit_code']==windows['launcher_result']['original_UI_restore_exit_code']==0
    servers={}
    for port,name in {7860:'webui',7861:'chat-webui',7862:'chat-natural-C1',7863:'chat-natural-C0',7864:'chat-answer-C1',7865:'chat-answer-C0'}.items():
        record_path=ROOT/f'reports/local/{name}/server.json';record=read_json(record_path)
        assert record['status']=='running' and alive(record)
        with urlopen(f'http://127.0.0.1:{port}/api/model',timeout=5) as response:api=json.load(response)
        assert not api['busy'] and api['parameters']==10001152
        if port==7860:assert api['checkpoint_sha256']==c['parent']['sha256']
        else:assert api['max_new_tokens']==32
        if port in (7864,7865):assert api['checkpoint_sha256']==training[api['arm']]['checkpoint']['sha256']
        servers[str(port)]=dict(identity=identity(record['pid']),HTTP=api,record=ref(record_path))
    base=servers['7860']['identity']['pid'];lock=Path.home()/'jmicro-data/gpu.lock'
    assert read_json(lock)['pid']==base;inode=str(lock.stat().st_ino)
    locks=[line for line in Path('/proc/locks').read_text().splitlines() if 'FLOCK' in line and 'WRITE' in line
        and line.split()[4]==str(base) and any(part.endswith(':'+inode) for part in line.split())]
    assert len(locks)==1
    dxg=[]
    for fd in (Path('/proc')/str(base)/'fd').iterdir():
        try:
            if os.readlink(fd)=='/dev/dxg':dxg.append(fd.name)
        except FileNotFoundError:pass
    assert dxg
    restoration=dict(observed_at=now(),servers=servers,actual_kernel_FLOCK=locks,Base_dxg_fds=dxg,
        scientific_process_alive=False,scientific_identity=job,Windows=ref(RUN/'windows_terminal_observation.json'),
        no_training_or_generation_by_this_check=True)
    save(RUN/'restoration_observation.json',restoration)
    stages=dict(reference=dict(passed=True,evidence=ref(PARENT_RUN/'reference_notes.json'),responses=80),
        capability_audit=dict(passed=True,evidence=ref(PARENT_RUN/'TRAIN_capability_review.json'),samples=120),
        memorization_diagnosis=dict(passed=True,evidence=ref(PARENT_RUN/'diagnostic-manifest-v2/completion.json'),generalization_not_certified=True),
        matched_SFT=dict(passed=True,config=ref(CONFIG),gate=ref(RUN/'native_gate.json'),gate_all_saved_fields_rechecked=gate_fields,
            training={arm:ref(RUN/arm/'training_audit.json') for arm in training}),
        unseen_and_actual_chat=dict(passed=True,analysis=ref(RUN/'final_analysis.json'),all_content_judgments=2628,
            manual_unique=manual,identical_raw_reused=reused,NLL_points=7,diagnostic_content_judgments=40,practical=practical,
            conditional_seed43=conditional_seed,restoration=ref(RUN/'restoration_observation.json')))
    save(target,dict(status='five_stage_answer_learning_trial_complete',created_at=now(),stages=stages,
        requested_five_steps_complete=all(v['passed'] for v in stages.values()),config=ref(CONFIG),analysis=ref(RUN/'final_analysis.json'),
        candidate_improvement_demonstrated=final['candidate_improvement_demonstrated'],
        candidate_all_absolute_DEV_screens_pass=final['candidate_all_absolute_DEV_screens_pass'],
        decision='Fixed trial completed; quality adoption remains separate',Chat_adopted=False,Base_adopted=False,protected_TEST_used=False,
        explicit_resource_amendment=c['resource_replan'],original3600_forecast_gate_failed_before_science=True,
        owned_GPU_stage_wall_seconds=ledger['total_seconds'],GPU_ledger=ref(RUN/'GPU_ledger.json'),
        independent_human_or_blind_TEST=False,formal_Base_fullpipeline_fullDEV440_and_newTEST_still_pending=True,source=ref(__file__)))
    print('All five stages proven complete from actual evidence; no quality adoption claim')


if __name__=='__main__':main()
