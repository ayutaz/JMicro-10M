"""Close plan149's first trial from completed evidence; never train or adopt."""
import json
import os
from pathlib import Path
import subprocess
import sys
from urllib.request import urlopen
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from chat_natural_contract import ROOT,RUN,CONFIG,ref,require_ref
from jmicro.experiment import read_json,sha256,now
from jmicro.training import atomic_json,implementation_hashes
from phase6_performance import identity,alive


def main():
    target=RUN/'completion.json'
    assert not target.exists(),'Preserve terminal completion evidence'
    c=read_json(CONFIG)
    assert sha256(CONFIG)=='ec0b61b2961ef9294cb840cb86ad6f5ba291ea1c4a0213d0404e9fa87cdb464d'
    assert c['implementation']==implementation_hashes()
    assert all(sha256(ROOT/p)==value for p,value in c['source_sha256'].items())
    for value in (c['parent'],c['tokenizer'],c['TRAIN_manifest'],c['TRAIN_QA'],c['DEV_preparation']):
        require_ref(value)
    qa=read_json(RUN/'TRAIN_QA_review.json')
    assert qa['samples']==len(qa['notes'])==300 and qa['rejected']==28
    final=read_json(RUN/'final_analysis.json')
    assert final['judgments']==2190 and final['config']['sha256']==sha256(CONFIG)
    assert not final['candidate_improvement_demonstrated'] and not final['candidate_all_absolute_DEV_screens_pass']
    manual=reused=0
    for suite,arms in final['summaries'].items():
        for arm,row in arms.items():
            for key in ('raw','notes','review'):require_ref(row[key])
            notes=read_json(row['notes']['path'])
            assert len(notes['judgments'])==219
            packet=read_json(RUN/'evaluation'/arm/suite/'packet.json')
            manual+=len(packet['pending']);reused+=len(packet['reused'])
    assert manual+reused==2190
    training={}
    for arm in ('C0','C1'):
        audit=read_json(RUN/arm/'training_audit.json')
        assert audit['passed'] and audit['updates']==1921
        require_ref(audit['checkpoint']);require_ref(audit['metrics'])
        for value in audit['checkpoints'].values():require_ref(value)
        assert read_json(RUN/f'{arm}_dry_run.json')['status']=='passed'
        practical=read_json(RUN/'practical'/arm/'raw.json')
        notes=read_json(RUN/'practical'/arm/'notes.json')
        require_ref(notes['raw'])
        assert len(practical['conversations'])==5 and sum(len(v['turns']) for v in practical['conversations'])==10
        assert notes['all10_reviewed'] and len(notes['judgments'])==10
        assert read_json(RUN/'practical'/arm/'UI_observation.json')['response_choices']==[16,32,64]
        for point in ('250000','500000'):
            diagnostic=read_json(RUN/'diagnostics'/arm/f'{point}_notes.json')
            assert diagnostic['all10_reviewed'] and len(diagnostic['judgments'])==10
            require_ref(diagnostic['raw']);require_ref(diagnostic['authored'])
        training[arm]=dict(audit=ref(RUN/arm/'training_audit.json'),checkpoint=audit['checkpoint'],
            Assistant_teachers=audit['Assistant_teachers'],step_wall_seconds=audit['actual_training_step_seconds'],
            practical_raw=ref(RUN/'practical'/arm/'raw.json'),practical_notes=ref(RUN/'practical'/arm/'notes.json'))
    for points in final['NLL'].values():
        for point in points.values():require_ref(point['source'])
    ledger=read_json(RUN/'GPU_ledger.json')
    assert len(ledger['entries'])==4 and all(row['status']=='complete' for row in ledger['entries'])
    assert all(row['seconds']<=ledger['limits_seconds'][row['category']] for row in ledger['entries'])
    old=dict(pid=468008,boot_id='4052bfc5-3850-44e4-9123-d34a9e19f36e',start_ticks='86194546')
    assert not alive(old)
    windows=read_json(RUN/'windows_terminal_observation.json')
    assert not windows['process_present'] and windows['launcher_result']['status']=='complete'
    assert windows['launcher_result']['exit_code']==windows['launcher_result']['original_UI_restore_exit_code']==0
    servers={}
    records={7860:'webui',7861:'chat-webui',7862:'chat-natural-C1',7863:'chat-natural-C0'}
    for port,name in records.items():
        server=read_json(ROOT/f'reports/local/{name}/server.json')
        assert server['status']=='running' and alive(server)
        with urlopen(f'http://127.0.0.1:{port}/api/model',timeout=5) as response:api=json.load(response)
        assert not api['busy'] and api['parameters']==10001152
        if port==7860:assert api['checkpoint_sha256']==c['parent']['sha256']
        else:assert api['max_new_tokens']==32
        if port in (7862,7863):assert api['checkpoint_sha256']==training[api['arm']]['checkpoint']['sha256']
        servers[str(port)]=dict(identity=identity(server['pid']),HTTP=api,record=ref(ROOT/f'reports/local/{name}/server.json'))
    base_pid=servers['7860']['identity']['pid']
    lock=Path.home()/'jmicro-data/gpu.lock'
    assert read_json(lock)['pid']==base_pid
    inode=str(lock.stat().st_ino)
    locks=[line for line in Path('/proc/locks').read_text().splitlines() if
        'FLOCK' in line and 'WRITE' in line and line.split()[4]==str(base_pid) and
        any(part.endswith(':'+inode) for part in line.split())]
    assert len(locks)==1
    dxg=[]
    for fd in (Path('/proc')/str(base_pid)/'fd').iterdir():
        try:
            if os.readlink(fd)=='/dev/dxg':dxg.append(fd.name)
        except FileNotFoundError:pass
    assert dxg
    peers=subprocess.run(['/usr/lib/wsl/lib/nvidia-smi','--query-compute-apps=pid,process_name,used_gpu_memory',
        '--format=csv,noheader,nounits'],capture_output=True,text=True,check=True).stdout.strip()
    conflicts=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:cmd=path.read_bytes().replace(b'\0',b' ').decode(errors='replace')
        except (FileNotFoundError,PermissionError,ProcessLookupError):continue
        if any(word in cmd for word in ('scripts/run_chat_natural.py','scripts/run_chat_lr.py',
            'scripts/run_chat_first_sft.py','scripts/run_chat_semantic.py','scripts/run_chat_generalization.py',
            'scripts/run_chat_improvement.py','scripts/run_rdrop_science.py')):
            conflicts.append(dict(pid=int(path.parent.name),command=cmd))
    assert not conflicts
    observation=dict(observed_at=now(),servers=servers,actual_kernel_FLOCK=locks,Base_dxg_fds=dxg,
        scientific_identity=old,scientific_process_alive=False,Windows=ref(RUN/'windows_terminal_observation.json'),
        NVML_compute_raw=peers,sole_global_GPU_peer_proven=False,conflicting_project_jobs=conflicts,
        no_training_or_generation_launched_by_this_check=True)
    atomic_json(RUN/'restoration_observation.json',observation)
    stages={
        '1_prepare_TRAIN':dict(passed=True,manifest=c['TRAIN_manifest'],QA=c['TRAIN_QA'],
            diversity=ref(RUN/'TRAIN_diversity_audit.json'),source_credits=ref(RUN/'source_credits.json')),
        '2_freeze_conditions':dict(passed=True,config=ref(CONFIG),native_gate=ref(RUN/'native_gate.json'),
            launch_amendment=ref(RUN/'launch_observation_amendment.json')),
        '3_train_matched_arms':dict(passed=True,arms=training),
        '4_complete_comparison':dict(passed=True,analysis=ref(RUN/'final_analysis.json'),all2190_judgments=True,
            authored_unique=manual,identical_raw_reused=reused,NLL_points=7,diagnostic_content_judgments=40),
        '5_actual_chat_delivery':dict(passed=True,practical_conversations=10,practical_responses=20,
            restoration=ref(RUN/'restoration_observation.json'),browser_render_automation=False,
            candidate_URL='http://127.0.0.1:7862',control_URL='http://127.0.0.1:7863',default_tokens=32,
            UI_choices=[16,32,64])}
    result=dict(status='first_matched_SFT_trial_completed_candidate_not_adopted',created_at=now(),stages=stages,
        requested_five_steps_complete=all(row['passed'] for row in stages.values()),
        config=ref(CONFIG),analysis=ref(RUN/'final_analysis.json'),GPU_ledger=ref(RUN/'GPU_ledger.json'),
        owned_GPU_stage_wall_seconds=ledger['total_seconds'],separate_one_token_UI_diagnostic_wall_seconds=.4761091,
        cumulative_local_GPU_budget_unlimited=True,original_per_run_caps_preserved=True,
        decision='Close this fixed condition: improvement not demonstrated, absolute Chat DEV screens fail',
        parent_checkpoint_unchanged=True,frozen_scientific_sources_unchanged=True,
        candidate_improvement_demonstrated=False,Chat_adopted=False,Base_adopted=False,protected_TEST_used=False,
        reader_scope_disclosure=ref(RUN/'reader_scope_disclosure.json'),
        review_limitations='Codex nonblind judgments on authored DEV, no independent human audit or blind TEST',
        formal_qualification_pending=['qualified Base recipe','Base retention/fullDEV/all440',
            'independent fresh Base whole pipeline seed43','independent SFT reproduction if promising',
            'new sealed TEST and formal adoption'],
        next_work_not_launched='Prospective TRAIN audit of direct answers and actual history/correction targets; no old-run extension',
        report=ref(ROOT/'docs/150_chat_natural_sft_results.md'),source=ref(Path(__file__)))
    atomic_json(target,result)
    print(json.dumps(dict(status=result['status'],steps_complete=result['requested_five_steps_complete'],
        manual=manual,reused=reused,Base_UI_pid=base_pid,GPU_stage_wall_seconds=ledger['total_seconds'])))


if __name__=='__main__':main()
