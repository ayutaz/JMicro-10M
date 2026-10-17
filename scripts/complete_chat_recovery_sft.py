"""Audit the four requested steps from actual evidence, without quality adoption."""
import csv
import json
import os
from pathlib import Path
from urllib.request import urlopen
import torch
from chat_recovery_contract import ROOT,RUN,CONFIG,SUITES,preflight
from answer_learning_common import save,ref,bound,read_json,now
from phase6_performance import alive,identity,finite_state
from jmicro.phase5 import equal_state
from review_chat_recovery_sft import wire
import review_chat_natural as reviewer
from review_chat_recovery_public100 import validate as public_validate,fingerprint as public_fp
from review_chat_recovery_aux import items as aux_items
from jmicro.chat_review import content_review


def main():
    target=RUN/'completion.json';assert not target.exists()
    c,_,_=preflight(False);wire();final=read_json(RUN/'final_analysis.json')
    assert final['config']==ref(CONFIG) and final['judgments']==3466 and not final['Chat_adopted']
    job=read_json(RUN/'pipeline.json');assert job['status']=='complete_raw_pending_content_and_browser' and not alive(job)
    assert read_json(RUN/'evaluation_raw_complete.json')['responses']==3466
    diagnosis=read_json(RUN.parent/'diagnostic_analysis.json')
    assert diagnosis['counts']==dict(new_control=200,prefix=100,history_finals=320,plain=120,conditional_NLL=640)
    assert diagnosis['source_sha256']==ref(ROOT/'scripts/review_chat_recovery_diagnostics.py')['sha256']
    for prefix,rawname,notesname,count,key in (
        ('control100','raw.json','notes.json',200,'all200_literal_judgments'),
        ('history','raw.json','notes.json',320,'judgments'),
        ('','plain_raw.json','plain_notes.json',120,'judgments'),
        ('','sampling_raw.json','sampling_notes.json',60,'judgments')):
        directory=RUN.parent/prefix;notes=read_json(directory/notesname)
        assert notes['raw_sha256']==ref(directory/rawname)['sha256'] and len(notes[key])==count
        assert all(len(n['rationale'])>=12 for n in notes[key])
    history=read_json(RUN.parent/'history/notes.json')
    assert len(history['prefix_reasons'])==100 and history['all_raw_prompt_IDs_bytes_histories_verified']
    assert len(read_json(RUN.parent/'history/likelihood.json')['rows'])==640
    gate=read_json(RUN/'native_gate.json');assert gate['passed'] and gate['technical_updates']==40 and gate['config_sha256']==ref(CONFIG)['sha256']
    gate_checks={};manual=reused=0;csv_rows=[]
    for arm in ('C0','C1'):
        proof=gate['arms'][arm];assert len(proof['all16_timing_updates'])==16 and all(proof['all_state_checks'].values())
        left=torch.load(bound(proof['branch_snapshots']['continuous']),map_location='cpu',weights_only=False)
        right=torch.load(bound(proof['branch_snapshots']['resumed']),map_location='cpu',weights_only=False)
        assert set(left)==set(right) and finite_state(left) and finite_state(right)
        checks={key:equal_state(left[key],right[key]) for key in left};assert all(checks.values());gate_checks[arm]=checks;del left,right
        audit=read_json(RUN/arm/'training_audit.json');assert audit['passed'] and audit['updates']==1929 and audit['Assistant_teachers']==1000000
        bound(audit['checkpoint']);bound(audit['metrics'])
        for kind,points in (('diagnostic',('250000','500000')),('practical',('250000',))):
            for point in points:
                raw,rows,authored_path,notes_path=aux_items(kind,arm,point);notes=read_json(notes_path)
                assert notes['raw']==ref(raw) and notes['authored']==ref(authored_path) and notes['all_reviewed']
                assert len(notes['judgments'])==len(rows)==(10 if kind=='diagnostic' else 18)
                assert read_json(authored_path)==[[n[k] for k in ('grammar','relevance','context','rationale')] for n in notes['judgments']]
        for suite in SUITES:
            path=RUN/'evaluation'/arm/suite/'result.json';raw,view,items=reviewer.get_items(path)
            notes=read_json(path.with_name('notes.json'));review=content_review(view,ref(path)['sha256'],notes,items)
            assert json.loads(json.dumps(review))==read_json(path.with_name('review.json'))
            packet=read_json(path.with_name('packet.json'));assert packet['evaluation_sha256']==ref(path)['sha256']
            bound(packet['review_adapter']);bound(packet['reuse_policy']);bound(notes['source'])
            manual+=len(packet['pending']);reused+=len(packet['reused']);ratings={n['key']:n for n in notes['judgments']}
            for key,item in items.items():
                n=ratings[key]
                if 'reuse' in n:
                    r=n['reuse'];assert reviewer.fingerprint(item)==r['fingerprint']
                    prior=ratings[r['same_packet_key']] if 'same_packet_key' in r else next(n for n in read_json(bound(r['source_notes']))['judgments'] if n['key']==r['source_notes']['key'])
                    assert all(n[k]==prior[k] for k in ('grammar','relevance','context','rationale'))
                csv_rows.append(dict(arm=arm,suite=suite,key=key,messages=json.dumps(item['messages'],ensure_ascii=False),response=item['response']['text'],
                    stop=item['response']['stop_reason'],**{k:n[k] for k in ('grammar','relevance','context','rationale')}))
            for key in ('raw','notes','review'):bound(final['summaries'][suite][arm][key])
        path,raw,_=public_validate(arm);notes=read_json(path.with_name('notes.json'));packet=read_json(path.with_name('packet.json'))
        assert notes['raw']==ref(path) and notes['packet']==ref(path.with_name('packet.json')) and packet['reviewer']==ref(ROOT/'scripts/review_chat_recovery_public100.py')
        assert len(notes['judgments'])==200;bound(notes['authored'])
        manual+=len(packet['pending']);reused+=len(packet['reused'])
        for row,n in zip(raw['responses'],notes['judgments'],strict=True):
            assert n['raw_fingerprint']==public_fp(row)
            if 'reuse' in n:bound(n['reuse']['source_notes'])
            csv_rows.append(dict(arm=arm,suite='public100',key=f'{row["id"]}-{row["turn"]}',messages=json.dumps(row['messages'],ensure_ascii=False),
                response=row['response']['text'],stop=row['response']['stop_reason'],**{k:n[k] for k in ('grammar','relevance','context','rationale')}))
    assert manual+reused==len(csv_rows)==3466
    for points in final['NLL'].values():
        for point in points.values():assert len(read_json(bound(point['source']))['targets'])==432
    if final['candidate_improvement_demonstrated']:
        reproduction=read_json(RUN/'seed43_reproduction.json');assert reproduction['complete'] and reproduction['seed']==43
        bound(reproduction['prospective_contract']);bound(reproduction['analysis']);conditional=ref(RUN/'seed43_reproduction.json')
    else:conditional='Not triggered: fixed positive new-content CI and no-count-regression criterion not satisfied'
    ledger=read_json(RUN/'GPU_ledger.json');assert len(ledger['entries'])==4 and all(r['status']=='complete' for r in ledger['entries'])
    for category,cap in c['limits_seconds'].items():assert sum(r['seconds'] for r in ledger['entries'] if r['category']==category)<=cap
    assert abs(ledger['total_seconds']-sum(r['seconds'] for r in ledger['entries']))<1e-8
    windows=read_json(RUN/'windows_terminal_observation.json');assert not windows['same_process_present']
    assert windows['launcher_result']['status']=='complete_raw_pending_content_and_browser'
    assert windows['launcher_result']['exit_code']==windows['launcher_result']['original_UI_restore_exit_code']==0
    servers={}
    ports={7860:'webui',7861:'chat-webui',7862:'chat-natural-C1',7863:'chat-natural-C0',7864:'chat-answer-C1',7865:'chat-answer-C0',7866:'chat-input-structure-C1',7867:'chat-input-structure-C0'}
    for port,name in ports.items():
        path=ROOT/f'reports/local/{name}/server.json';record=read_json(path);assert record['status']=='running' and alive(record)
        with urlopen(f'http://127.0.0.1:{port}/api/model',timeout=5) as response:api=json.load(response)
        assert not api['busy'] and api['parameters']==10001152
        if port==7860:assert api['checkpoint_sha256']==c['parent']['sha256']
        else:assert api['max_new_tokens']==32
        if port in (7866,7867):assert api['config_sha256']==ref(CONFIG)['sha256'] and api['checkpoint_sha256']==read_json(RUN/api['arm']/'training_audit.json')['checkpoint']['sha256']
        servers[str(port)]=dict(identity=identity(record['pid']),HTTP=api,record=ref(path))
    base=servers['7860']['identity']['pid'];lock=Path.home()/'jmicro-data/gpu.lock';assert read_json(lock)['pid']==base;inode=str(lock.stat().st_ino)
    locks=[line for line in Path('/proc/locks').read_text().splitlines() if 'FLOCK' in line and 'WRITE' in line and line.split()[4]==str(base) and any(t.endswith(':'+inode) for t in line.split())];assert len(locks)==1
    dxg=[]
    for fd in (Path('/proc')/str(base)/'fd').iterdir():
        try:
            if os.readlink(fd)=='/dev/dxg':dxg.append(fd.name)
        except FileNotFoundError:pass
    assert dxg
    restoration=RUN/'restoration_observation.json';save(restoration,dict(observed_at=now(),servers=servers,actual_kernel_FLOCK=locks,Base_dxg_fds=dxg,scientific_process_alive=False))
    csv_path=RUN/'all3466_responses.csv'
    with csv_path.open('x',encoding='utf-8-sig',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(csv_rows[0]));writer.writeheader();writer.writerows(csv_rows)
    save(target,dict(status='four_requested_steps_complete',created_at=now(),config=ref(CONFIG),analysis=ref(RUN/'final_analysis.json'),
        steps=dict(control100=ref(RUN.parent/'control100/notes.json'),factor_diagnosis=ref(RUN.parent/'diagnostic_analysis.json'),
            paired_SFT=dict(gate=ref(RUN/'native_gate.json'),all_saved_gate_fields_rechecked=gate_checks,training={a:ref(RUN/a/'training_audit.json') for a in ('C0','C1')}),
            unseen_and_actual_chat=dict(all3466_judgments=True,manual=manual,reused_identical_raw=reused,intermediate_judgments=40,browser_judgments=36,NLL_targets432_at7points=True,
                practical={a:ref(RUN/'practical'/a/'notes.json') for a in ('C0','C1')},conditional_seed43=conditional)),
        CSV=ref(csv_path),restoration=ref(restoration),Windows=ref(RUN/'windows_terminal_observation.json'),GPU_ledger=ref(RUN/'GPU_ledger.json'),GPU_stage_wall_seconds=ledger['total_seconds'],
        candidate_improvement_demonstrated=final['candidate_improvement_demonstrated'],candidate_all_absolute_DEV_screens_pass=final['candidate_all_absolute_DEV_screens_pass'],
        Chat_adopted=False,Base_adopted=False,protected_TEST_used=False,independent_human_or_blind_TEST=False,
        formal_Base_fullpipeline_fullDEV440_newTEST_still_pending=True,source=ref(__file__)))
    print('Four requested steps audited; trial completion and quality adoption remain separate')


if __name__=='__main__':main()
