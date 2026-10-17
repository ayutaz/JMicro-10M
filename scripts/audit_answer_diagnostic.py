"""Inspect complete native states, all histories and64 literal content notes."""
import json
from pathlib import Path
import torch
from answer_learning_common import ROOT,RUN,ref,bound,read_json,save,now,sha256
from answer_diagnostic_manifest_v2 import CONFIG,DIRECTORY,OLD_DIRECTORY
from phase6_performance import alive,finite_state,identity
from jmicro.tokenizer import Tokenizer
from jmicro.phase5 import equal_state
from review_chat_natural import validate_reply
from urllib.request import urlopen


def main():
    target=DIRECTORY/'completion.json';assert not target.exists()
    c=read_json(CONFIG);result=read_json(DIRECTORY/'result.json');job=read_json(DIRECTORY/'job.json')
    assert job['status']=='complete' and not alive(job) and result['full_state_CPU_replay_exact']
    assert all(sha256(ROOT/p)==v for p,v in c['source_sha256'].items())
    state=torch.load(bound(result['checkpoint']),map_location='cpu',weights_only=False)
    assert finite_state(state) and state['update']==478 and state['supervised_tokens']==250018
    dry=read_json(bound(c['CPU_replay']));assert state['sampler']==dry['sampler_terminal']
    assert state['lineage']['base_checkpoint']==c['parent'] and state['lineage']['optimizer_policy']=='fresh'
    assert state['shard_manifest_sha256']==c['data_manifest']['sha256'] and state['implementation_sha256']==c['implementation']
    assert len(state['optimizer']['state'])==119 and all(int(v['step'])==478 for v in state['optimizer']['state'].values())
    assert state['scheduler']['last_epoch']==478 and set(state['rng'])=={'python','numpy','torch','cuda'}
    history=[json.loads(line) for line in (DIRECTORY/'metrics.jsonl').read_text().splitlines()]
    assert len(history)==len(dry['history'])==478
    for a,b in zip(history,dry['history'],strict=True):
        assert (a['update'],a['teachers_this_update'],a['microbatches'],a['lr'],a['supervised_tokens'])==(b['update'],b['teachers_this_update'],b['microbatches'],b['lr'],b['teachers'])
    left=torch.load(DIRECTORY/'probe_continuous.pt',map_location='cpu',weights_only=False)
    right=torch.load(DIRECTORY/'probe_resumed.pt',map_location='cpu',weights_only=False)
    assert equal_state(left,right),'Compare every checkpoint field, not just named numerical subsets'
    tok=Tokenizer(bound(c['tokenizer']));cases=read_json(bound(c['cases']))
    authored=read_json(RUN/'diagnostic_authored.json');assert len(authored)==32
    before=read_json(DIRECTORY/'before_raw.json');after=read_json(DIRECTORY/'after_raw.json')
    summaries={};judgments={}
    for name,raw,offset in (('before',before,1),('after',after,5)):
        assert len(raw['outputs'])==32 and raw['config']['sha256']==sha256(CONFIG)
        notes=[]
        for case,item,score in zip(cases,raw['outputs'],authored,strict=True):
            assert item['case']==case and score[0]==case['id']
            validate_reply(item['response'],tok,case['messages'],True)
            g,r,ctx,reason=score[offset:offset+4]
            assert all(type(v) is int and v in (0,1,2) for v in (g,r,ctx)) and len(reason)>=12
            notes.append(dict(id=case['id'],grammar=g,relevance=r,context=ctx,rationale=reason))
        judgments[name]=notes
        summaries[name]=dict(responses=32,content=sum(n['grammar']==n['relevance']==2 for n in notes),
            direct_content=sum(n['grammar']==n['relevance']==2 and case['direct_answer'] for n,case in zip(notes,cases)),
            natural_stop=sum(row['response']['stop_reason'] in ('eot','eos') for row in raw['outputs']),
            target_exact=sum(row['response']['text']==row['case']['target'] for row in raw['outputs']),mean_NLL=raw['mean_NLL'])
    acceptance=c['acceptance'];a=summaries['after']
    passed=a['content']>=acceptance['content_minimum'] and a['direct_content']>=acceptance['direct_answer_minimum'] and a['natural_stop']>=acceptance['natural_stop_minimum']
    server=read_json(ROOT/'reports/local/webui/server.json');assert alive(server) and server['status']=='running'
    with urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response:api=json.load(response)
    assert not api['busy'] and api['checkpoint_sha256']==c['parent']['sha256']
    lock=Path.home()/'jmicro-data/gpu.lock';assert read_json(lock)['pid']==server['pid'];inode=str(lock.stat().st_ino)
    assert any('FLOCK' in line and 'WRITE' in line and line.split()[4]==str(server['pid']) and any(t.endswith(':'+inode) for t in line.split()) for line in Path('/proc/locks').read_text().splitlines())
    ledger=read_json(DIRECTORY/'GPU_ledger.json');assert ledger['entries'][0]['seconds']==c['inherited_probe_seconds']
    assert all(sum(r['seconds'] for r in ledger['entries'] if r['stage']==key)<=cap for key,cap in c['limits_seconds'].items())
    save(target,dict(status='all32_TRAIN_memorization_diagnosis_complete',passed=passed,created_at=now(),config=ref(CONFIG),
        checkpoint=result['checkpoint'],authored=ref(RUN/'diagnostic_authored.json'),before=ref(DIRECTORY/'before_raw.json'),
        after=ref(DIRECTORY/'after_raw.json'),judgments=judgments,summaries=summaries,
        all478_updates_and_all119_Adam_states_verified=True,whole_probe_checkpoints_exact=True,
        scientific_process_terminal=True,Base_UI_identity=identity(server['pid']),Base_idle_HTTP=api,actual_kernel_FLOCK_verified=True,
        GPU_ledger=ref(DIRECTORY/'GPU_ledger.json'),all_carried_GPU_stage_wall_seconds=ledger['total_seconds'],
        failed_technical_packaging_preserved=ref(OLD_DIRECTORY/'job.json'),
        conclusion='Learning this small reviewed TRAIN set is demonstrated; unseen generalization remains untested',
        scope_limit='32 memorized TRAIN prompts, six direct answers; no unseen memory/correction capability proof',
        reviewer='Codex nonblind; all64 raw replies individually judged',protected_TEST_used=False,Chat_adopted=False))
    print(json.dumps(dict(passed=passed,summaries=summaries,wall_seconds=ledger['total_seconds'],Base_UI_pid=server['pid'])))


if __name__=='__main__':main()
