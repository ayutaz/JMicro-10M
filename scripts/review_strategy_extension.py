"""Audit conditional300M endpoints, common evaluation and individual reviews."""
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
from run_strategy_extension import RUN,BASE,CONFIG,load_config
import run_curriculum_strategy as original


def audit():
    ext=load_config();c=original.load_config();result=read_json(RUN/'compare-result.json');job=read_json(RUN/'job.json')
    assert job['status']=='complete' and not alive(job) and job['config_sha256']==result['config_sha256']==sha256(CONFIG)
    assert result['gpu_seconds']<=job['gpu_elapsed_seconds'] and ext['prior_GPU_seconds']+job['gpu_elapsed_seconds']<=1800
    assert result['scientific_teacher_tokens']==400000000 and result['cumulative_scientific_teacher_tokens']==600000000
    assert not result['protected_test_used']
    annotation=read_json(RUN/'annotations.json');old=read_json(BASE/'compare-result.json');old_notes=read_json(BASE/'annotations.json')
    tok=Tokenizer(ROOT/c['tokenizer']);cases={json.loads(s)['id']:json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines() if json.loads(s)['split']=='dev'}
    summaries={};scores={};gates={};verification=0;states=[]
    for arm,detail in result['checkpoints'].items():
        assert sha256(Path(detail['checkpoint']))==detail['checkpoint_sha256']
        state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
        parent=torch.load(ext['parents'][arm]['path'],map_location='cpu',weights_only=False)
        assert finite_state(state) and all(k in state for k in ('optimizer','scheduler','rng','sampler','lineage','token_digest'))
        assert state['pilot_binding']==detail['binding'] and state['sampler']['source_teachers']==ext['goals']
        lineage=state['lineage']
        assert lineage['parent_update']==parent['update'] and lineage['parent_tokens']==parent['tokens']
        assert equal_state(lineage['extension_parent_sampler'],parent['sampler'])
        assert equal_state(lineage['extension_parent_lineage'],parent['lineage'])
        assert equal_state(lineage['extension_parent_scheduler'],parent['scheduler'])
        assert lineage['optimizer_policy']=='inherit' and state['pilot_binding']['warmup_updates']==0
        assert state['supervised_tokens']-parent['supervised_tokens']==detail['additional_supervised_tokens']==200000000
        assert state['tokens']-parent['tokens']==detail['additional_input_tokens']==sum(state['sampler']['source_tokens'].values())
        assert sum(state['sampler']['source_physical_tokens'].values())==detail['physical_input_tokens']
        history=[json.loads(s) for s in (RUN/arm/'metrics.jsonl').read_text().splitlines()]
        assert len(history)==state['update']-parent['update']==state['sampler']['position']
        assert [r['update'] for r in history]==list(range(parent['update']+1,state['update']+1))
        assert state['token_digest']==history[-1]['token_digest']
        consumed=0
        for r in history:
            assert math.isclose(r['lr'],teacher_lr(consumed,200000000,c['strategies'][arm]['peak_lr']),rel_tol=1e-12)
            assert math.isfinite(r['loss']) and math.isfinite(r['gradient_norm'])
            consumed=sum(r['source_teachers'].values())
        assert consumed==200000000
        gate=read_json(RUN/'resume-gate'/arm/'result.json');assert gate['passed'] and all(gate['checks'].values())
        verification+=gate['verification_teacher_tokens']
        ev=result['evaluations'][arm];rows=ev['generation']['outputs'];validate_rows(rows,tok)
        assert len(rows)==80 and {r['id'] for r in rows}==set(cases)
        assert all(r['prefix']==cases[r['id']]['prefix'] for r in rows)
        assert ev['checkpoint_sha256']==detail['checkpoint_sha256'] and ev['binding']==detail['binding']
        assert ev['evaluation_RNG_isolated'] and not ev['protected_test_used'] and ev['greedy_rates']==rate(rows)
        body=ev['body'];assert body['documents']==len(body['rows'])==256
        assert body['body_bytes']==472055 and body['body_tokens']==122343 and all(r['body_tokens']==r['scored_body_tokens'] for r in body['rows'])
        assert math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/472055,rel_tol=1e-12)
        assert [(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in body['rows']]==[(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in old['evaluations'][arm]['body']['rows']]
        assert all(ev['diagnostics'][k]['complete'] and ev['diagnostics'][k]['count']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items())
        entry=annotation['arms'][arm];assert entry['generation_sha256']==sha256(RUN/'evaluation'/arm/'evaluation/generation.json')
        notes=entry['notes'];scores[arm]={n[0]:dict(grammar=n[1],relevance=n[2],coherence=n[3],completion=n[4],rationale=n[5]) for n in notes}
        assert len(notes)==len(scores[arm])==80 and set(scores[arm])==set(cases)
        assert all(s['rationale'] and all(s[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and s['completion'] in (0,1) for s in scores[arm].values())
        assert all(not scores[arm][r['id']]['completion'] or r['stop_reason']=='stop_id' for r in rows)
        prior={n[0]:dict(grammar=n[1],relevance=n[2],coherence=n[3],completion=n[4],rationale=n[5]) for n in old_notes['arms'][arm]['notes']}
        summary=dict(BPB=body['bpb'],rates=ev['greedy_rates'],Japanese={k:ev['diagnostics'][k]['primary']['accuracy'] for k in ('semantics','jblimp','jcqa')},
            grammar2=sum(s['grammar']==2 for s in scores[arm].values()),relevance2=sum(s['relevance']==2 for s in scores[arm].values()),
            coherent=sum(s['coherence']==2 for s in scores[arm].values()),appropriate=sum(s['completion'] for s in scores[arm].values()),
            auxiliary=result['auxiliary'][arm]['summary'],additional_teacher_tokens=200000000,cumulative_teacher_tokens=300000000,
            valid_input_tokens=detail['additional_input_tokens'],physical_tokens=detail['physical_input_tokens'],
            seconds=detail['training_seconds'],peak_allocated_bytes=detail['peak_allocated_bytes'],EOS_teachers=detail['source_eos_teachers'])
        summaries[arm]=summary
        practical=dict(coherence_at_least27=summary['coherent']>=27,appropriate_at_least27=summary['appropriate']>=27,
            EOS_at_least37=ev['greedy_rates']['eos']>=37,repetition_at_most18=ev['greedy_rates']['repetition']<=18)
        relative=quality_gates(old['evaluations'][arm],ev,prior,scores[arm],'content')
        original_gate=adoption_checks(read_json(Path(c['reference']['web_screen']['path'])),ev)
        gates[arm]=dict(practical=practical,relative_to100M=relative,original_Web=original_gate,
            adopted=all(practical.values()) and relative['passed'] and all(original_gate.values()))
        states.append(state['sampler']);del state,parent
    assert verification==result['verification_teacher_tokens']
    assert states[0]['source_eos']==states[1]['source_eos'] and states[0]['short']==states[1]['short']
    report=dict(status='verified_learning_and_content_evidence',summaries=summaries,gates=gates,
        between_strategies=quality_gates(result['evaluations']['fresh'],result['evaluations']['continuation'],scores['fresh'],scores['continuation'],'content'),
        scientific_teacher_tokens=400000000,cumulative_scientific_teacher_tokens=600000000,
        verification_teacher_tokens=verification,gpu_seconds=result['gpu_seconds'],stage3_total_GPU_seconds=ext['prior_GPU_seconds']+job['gpu_elapsed_seconds'],
        result_sha256=sha256(RUN/'compare-result.json'),annotations_sha256=sha256(RUN/'annotations.json'),
        decision='No more extension in this scope; retain original UI unless all unchanged adoption gates pass',
        interpretation='Learning strategy comparison with staged reheat, not capacity proof or uninterrupted300M; auxiliary Web may be parent-known; official dev remains separate',
        numerical_failures72_unchanged=True,independent_human_blind=False,protected_test_used=False,created_at=now())
    write_json(RUN/'review.json',report);write_json(ROOT/'reports/phase6/strategy_extension_review.json',report)
    print(json.dumps(dict(summaries=summaries,gates=gates),ensure_ascii=False),flush=True)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2);audit()
