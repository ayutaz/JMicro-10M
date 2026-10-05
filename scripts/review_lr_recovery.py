"""Actual matched LR forks, full-state accounting and all160 content judgments."""
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.packing_study import teacher_lr
from jmicro.tokenizer import Tokenizer
from phase6_performance import finite_state,alive
from review_eos_5b_finish import validate_rows
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import rate,equal_state
from run_lr_recovery import RUN,OLD,BASE,CONFIG,load_config
import run_curriculum_strategy as strategy


def audit():
    c=load_config();recipe=strategy.load_config();result=read_json(RUN/'compare-result.json');job=read_json(RUN/'job.json')
    assert job['status']=='complete' and not alive(job)
    assert result['config_sha256']==job['config_sha256']==sha256(CONFIG)
    assert result['scientific_teacher_tokens']==400000000 and result['gpu_seconds']<=job['gpu_elapsed_seconds']<=c['gpu_budget_seconds']
    assert not result['requested_five_steps_complete'] and not result['protected_test_used']
    reference=read_json(OLD/'compare-result.json');old_notes=read_json(OLD/'annotations.json')
    tok=Tokenizer(ROOT/recipe['tokenizer']);cases={r['id']:r for r in (json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    annotations=dict(reviewer='Codex nonblind',independent_human_blind=False,arms={});summary={};states=[];verification=0
    for arm,d in result['checkpoints'].items():
        path=Path(d['checkpoint']);assert sha256(path)==d['checkpoint_sha256']
        state=torch.load(path,map_location='cpu',weights_only=False)
        parent=torch.load(c['parents'][arm]['path'],map_location='cpu',weights_only=False)
        assert finite_state(state) and all(k in state for k in ('optimizer','scheduler','rng','sampler','lineage','token_digest'))
        assert state['pilot_binding']==d['binding'] and state['sampler']['source_teachers']==c['goals']
        assert state['supervised_tokens']-parent['supervised_tokens']==d['additional_supervised_tokens']==200000000
        assert state['tokens']-parent['tokens']==d['additional_input_tokens']==sum(state['sampler']['source_tokens'].values())
        assert sum(state['sampler']['source_physical_tokens'].values())==d['physical_input_tokens']
        assert equal_state(state['lineage']['extension_parent_sampler'],parent['sampler'])
        assert state['lineage']['cold_schedule']['parent_actual_lr']==c['peak_lr'][arm]==parent['optimizer']['param_groups'][0]['lr']
        assert state['lineage']['optimizer_policy']=='inherit' and d['binding']['warmup_updates']==0
        history=[json.loads(s) for s in (RUN/arm/'metrics.jsonl').read_text().splitlines()]
        assert len(history)==state['update']-parent['update']==state['sampler']['position']
        assert [r['update'] for r in history]==list(range(parent['update']+1,state['update']+1))
        assert state['token_digest']==history[-1]['token_digest']
        consumed=0
        for r in history:
            assert math.isclose(r['lr'],teacher_lr(consumed,200000000,c['peak_lr'][arm]),rel_tol=1e-12)
            assert math.isfinite(r['loss']) and math.isfinite(r['gradient_norm'])
            consumed=sum(r['source_teachers'].values())
        assert consumed==200000000
        control=reference['checkpoints'][arm]
        assert d['source_teachers']==control['source_teachers'] and d['source_eos_teachers']==control['source_eos_teachers']
        assert equal_state(d['sampler']['short'],control['sampler']['short'])
        control_state=torch.load(control['checkpoint'],map_location='cpu',weights_only=False)
        assert state['token_digest']==control_state['token_digest']
        gate=read_json(RUN/'resume-gate'/arm/'result.json');assert gate['passed'] and all(gate['checks'].values())
        verification+=gate['verification_teacher_tokens']
        ev=result['evaluations'][arm];rows=ev['generation']['outputs'];validate_rows(rows,tok)
        assert len(rows)==80 and {r['id'] for r in rows}==set(cases)
        assert all(r['prefix']==cases[r['id']]['prefix'] for r in rows)
        assert ev['checkpoint_sha256']==d['checkpoint_sha256'] and ev['binding']==d['binding']
        assert ev['evaluation_RNG_isolated'] and not ev['protected_test_used'] and ev['greedy_rates']==rate(rows)
        body=ev['body'];assert body['documents']==len(body['rows'])==256 and body['body_bytes']==472055 and body['body_tokens']==122343
        assert all(r['body_tokens']==r['scored_body_tokens'] for r in body['rows'])
        assert math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/472055,rel_tol=1e-12)
        assert [(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in body['rows']]==[(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in reference['evaluations'][arm]['body']['rows']]
        assert all(ev['diagnostics'][k]['complete'] and ev['diagnostics'][k]['count']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items())
        notes_path=ROOT/f'reports/phase6/lr_recovery_{arm}_notes.json';notes=read_json(notes_path)['notes']
        scores={n[0]:dict(grammar=n[1],relevance=n[2],coherence=n[3],completion=n[4],rationale=n[5]) for n in notes}
        assert len(notes)==len(scores)==80 and set(scores)==set(cases)
        assert all(s['rationale'] and all(s[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and s['completion'] in (0,1) for s in scores.values())
        assert all(not scores[r['id']]['completion'] or r['stop_reason']=='stop_id' for r in rows)
        annotations['arms'][arm]=dict(notes=notes,generation_sha256=sha256(RUN/'evaluation'/arm/'evaluation/generation.json'),notes_sha256=sha256(notes_path))
        prior={n[0]:dict(grammar=n[1],relevance=n[2],coherence=n[3],completion=n[4],rationale=n[5]) for n in old_notes['arms'][arm]['notes']}
        relative=quality_gates(reference['evaluations'][arm],ev,prior,scores,'content')
        original_gate=adoption_checks(read_json(Path(recipe['reference']['web_screen']['path'])),ev)
        coherent=sum(s['coherence']==2 for s in scores.values());appropriate=sum(s['completion'] for s in scores.values())
        practical=dict(coherence_at_least27=coherent>=27,appropriate_at_least27=appropriate>=27,EOS_at_least37=ev['greedy_rates']['eos']>=37,repetition_at_most18=ev['greedy_rates']['repetition']<=18)
        old_ev=reference['evaluations'][arm]
        BPB_improved=body['bpb']<=old_ev['body']['bpb']*.99
        no_new_failures=all(ev['greedy_rates'][k]<=old_ev['greedy_rates'][k] for k in ('unicode_failure','role_leak','empty'))
        summary[arm]=dict(BPB=body['bpb'],reheat_BPB=old_ev['body']['bpb'],BPB_relative_improvement=1-body['bpb']/old_ev['body']['bpb'],
            rates=ev['greedy_rates'],Japanese={k:ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics','jblimp','jcqa')},
            coherent=coherent,appropriate=appropriate,practical=practical,relative=relative,original_Web=original_gate,
            low_LR_preferred_for_recipe=BPB_improved and no_new_failures,
            safety_interpretation='No increase in raw failure counts; case IDs retained, this is not proof all failures were repaired',
            adopted=all(practical.values()) and relative['passed'] and all(original_gate.values()),
            scientific_teachers=200000000,valid_input_tokens=d['additional_input_tokens'],physical_tokens=d['physical_input_tokens'],
            seconds=d['training_seconds'],peak_allocated_bytes=d['peak_allocated_bytes'],additional_EOS_teachers=d['source_eos_teachers'])
        states.append(state['sampler']);del state,parent,control_state
    assert verification==result['verification_teacher_tokens']
    assert equal_state(states[0]['short'],states[1]['short'])
    write_json(RUN/'annotations.json',annotations);write_json(ROOT/'reports/phase6/lr_recovery_annotations.json',annotations)
    h=read_json(RUN/'history-probe.json')
    history={arm:{split:{k:r[k] for k in ('body_bytes','BPB','EOS','repeated4gram')} for split,r in entry.items() if split in ('train','dev')} for arm,entry in h['results'].items()}
    report=dict(status='stage1_evidence_complete',summaries=summary,history=history,scientific_teacher_tokens=400000000,
        verification_teacher_tokens=verification,CUDA_verification_optimizer_updates=16,gpu_seconds=result['gpu_seconds'],
        result_sha256=sha256(RUN/'compare-result.json'),annotations_sha256=sha256(RUN/'annotations.json'),
        decision='Proceed to distinct-source material comparison; retain original accepted UI until unchanged quality gates pass',
        interpretation='Exact same teacher order/state fork, entire LR scale differs10x; not proof of reheat instant-only effect or best fresh-from-zero LR',
        numerical_failures72_unchanged=True,independent_human_blind=False,requested_five_steps_complete=False,protected_test_used=False,created_at=now())
    write_json(RUN/'review.json',report);write_json(ROOT/'reports/phase6/lr_recovery_review.json',report)
    print(json.dumps(dict(summaries=summary,history=history),ensure_ascii=False),flush=True)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2);audit()
