"""One model-only midpoint, original raw80 and all unchanged Base gates."""
from pathlib import Path
import sys
import math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive
from run_weight_average_comparison import RUN,CONFIG,ARM,contract
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks


def main():
    c,base=contract();job=read_json(RUN/'job.json');result=read_json(RUN/'result.json');ev=result['evaluation']
    if (job['status']!='complete' or alive(job) or job['GPU_elapsed_seconds']>300
            or result['config_sha256']!=sha256(CONFIG) or result['GPU_seconds']>job['GPU_elapsed_seconds']
            or result['optimizer_updates'] or result['new_scientific_teacher_tokens'] or result['protected_test_used']):
        raise ValueError('Actual terminal bound read-only midpoint required')
    raw=RUN/f'evaluation/{ARM}/evaluation/generation.json';notes_path=RUN/'content-notes.json'
    if read_json(raw)!=ev['generation'] or ev['checkpoint_sha256']!=result['checkpoint']['sha256']:
        raise ValueError('Actual midpoint raw binding differs')
    rows=ev['generation']['outputs'];validate_rows(rows,Tokenizer(ROOT/base['tokenizer']))
    import json
    cases={r['id']:r for r in (json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    if len(rows)!=80 or {r['id'] for r in rows}!=set(cases) or any(r['prefix']!=cases[r['id']]['prefix'] for r in rows):
        raise ValueError('Original complete dev80 required')
    scores=validate_notes(rows,read_json(notes_path),sha256(raw))
    body=ev['body']
    if (body['documents']!=256 or body['body_tokens']!=122343 or body['body_bytes']!=472055 or len(body['rows'])!=256
            or any(r['body_tokens']!=r['scored_body_tokens'] or not math.isfinite(r['body_nll']) for r in body['rows'])
            or not math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/472055,rel_tol=1e-12)):
        raise ValueError('Same common bytes/whole256 required')
    if any(not ev['diagnostics'][k]['complete'] or ev['diagnostics'][k]['count']!=n for k,n in dict(semantics=192,jblimp=331,jcqa=1119).items()):
        raise ValueError('Complete Japanese diagnostics required')
    if any(t['evaluated_requests']!=512 or not all(t['checks'].values()) for t in result['transfer'].values()):
        raise ValueError('Both actual transfer128 suites required')
    control=read_json(Path(c['refs']['completed_result']['path']))['evaluations']['source_order']
    control_raw=ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/generation.json'
    a=validate_notes(control['generation']['outputs'],read_json(Path(c['refs']['strong_notes']['path'])),sha256(control_raw))
    if ([(r['id'],r['prefix']) for r in control['generation']['outputs']] != [(r['id'],r['prefix']) for r in rows]
            or [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in control['body']['rows']] != [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in body['rows']]):
        raise ValueError('Matched original controlIDs/bytes required')
    relative=quality_gates(control,ev,a,scores,'content')
    rates=ev['greedy_rates'];summary=dict(BPB=body['bpb'],rates=rates,
        grammar2=sum(n['grammar']==2 for n in scores.values()),relevance2=sum(n['relevance']==2 for n in scores.values()),
        coherent=sum(n['coherence']==2 for n in scores.values()),appropriate=sum(n['completion'] for n in scores.values()),
        Japanese={k:ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics','jblimp','jcqa')})
    absolute=dict(grammar_at_least56=summary['grammar2']>=56,coherence_at_least27=summary['coherent']>=27,
        appropriate_at_least27=summary['appropriate']>=27,EOS_at_least37=rates['eos']>=37,repetition_at_most18=rates['repetition']<=18,
        no_empty_role_unicode=all(rates[k]==0 for k in ('empty','role_leak','unicode_failure')))
    original=adoption_checks(read_json(Path(c['refs']['historical_Web_evaluation']['path'])),ev)
    eligible=relative['passed'] and all(absolute.values()) and all(original.values())
    report=dict(status='single_midpoint_all80_and_unchanged_gates_reviewed',created_at=now(),config_sha256=sha256(CONFIG),
        result_sha256=sha256(RUN/'result.json'),generation_sha256=sha256(raw),notes_sha256=sha256(notes_path),
        summary=summary,quality_comparison=relative,absolute_dev_screen=absolute,original_Web=original,
        eligible_for_final_Base_validation=eligible,all80_individually_read=True,independent_human_blind=False,
        scientific_teacher_tokens=0,optimizer_updates=0,GPU_seconds=job['GPU_elapsed_seconds'],
        protected_test_used=False,quality_criteria_unchanged=True,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,
        next_action='Independent learned recipe seed/full dev/protected test/adoption only if eligible; otherwise terminate this fixed midpoint without coefficient or endpoint sweep.')
    if (RUN/'review.json').exists():raise ValueError('Preserve terminal midpoint review')
    atomic_json(RUN/'review.json',report);atomic_json(ROOT/'reports/phase6/weight_average_comparison_review.json',report)
    print(dict(summary=summary,eligible=eligible))


if __name__=='__main__':main()
