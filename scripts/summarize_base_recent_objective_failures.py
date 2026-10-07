"""Bounded CPU-only companion to the frozen historical Base failure synthesis."""
import json
from pathlib import Path
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive


def main():
    started=time.monotonic(); phase=ROOT/'reports/phase6'
    target=phase/'base_recent_objective_failure_synthesis.json'
    if target.exists(): raise ValueError('Preserve original companion synthesis')
    rows=[]; control=None
    for key,name in [('on_policy_teacher','base_on_policy_teacher_comparison_completion.json'),
                     ('sam','base_sam_comparison_completion.json'),
                     ('middle_supervision','base_middle_supervision_comparison_completion.json')]:
        path=phase/name; r=read_json(path)
        if (alive(r['actual_identity']) or r['scientific_CE_teacher_tokens']!=100000000 or
            r['eligible_for_final_Base_validation'] is not False or r['all80_individually_read'] is not True or
            any(r[k] is not False for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_scored'))):
            raise ValueError('Exited fully reviewed rejected same100M evidence required')
        candidate=r['summaries'][key]
        if control is None: control=r['summaries']['CE']
        elif r['summaries']['CE']!=control: raise ValueError('Cached control changed')
        review=read_json(Path(r['review']['path']))
        if sha256(Path(r['review']['path']))!=r['review']['sha256']: raise ValueError('Saved review changed')
        rows.append(dict(condition=key,completion=dict(path=str(path),sha256=sha256(path)),
            original_gold_positions=100000000,new_unique_corpus=0,candidate=candidate,
            matched_gates=review['matched_objective_quality'],absolute_gates=review['absolute_dev_screen'],
            historical_Web=review['original_Web'],GPU_seconds_including_probe=r['total_GPU_seconds_including_probe']))
    old=phase/'base_failure_route_synthesis.json'
    if time.monotonic()-started>30: raise TimeoutError('CPU synthesis30s exceeded')
    output=dict(status='three_recent_native_same100M_objective_conditions_rejected',created_at=now(),
        historical_synthesis=dict(path=str(old),sha256=sha256(old)),historical_synthesis_changed=False,
        cached_control=control,conditions=rows,
        conclusions=['No candidate is an adopted Base. All3 original100M comparisons remain rejected under the same quality gates.',
            'On-policy feedback, same-batch perturbation and intermediate CE did not establish free-generation coherence gains. Small choice-score or repetition changes are not Base completion.',
            'These results do not prove data insufficiency, an architecture limit or overconfidence as the sole cause. No failed source/parent/optimizer/layer coefficient sweep should be restarted.'],
        next_candidate='One prospective confidence-penalty condition: original CE plus0.1 KL(p||native full-vocab uniform). Distinct KL direction and unchanged hard-label CE versus closed uniform-label smoothing. Existing repetition makes this worth a bounded test but is not evidence of a causal calibration defect. Not selected by old DEV scores or an optimized coefficient.',
        next_action='Implement independent analytic-loss/gradient/masking, CPU fullstate and CUDA save/resume/capacity/budget gate before a single same100M study. Preserve cachedCE/strong/absolute/historicalWeb and final independentseed/fullDEV/protectedTEST/adoption requirements.',
        CPU_seconds=time.monotonic()-started,GPU_seconds=0,new_scientific_gold_positions=0,new_content_judgments=0,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True,
        limitations='Repeated fixed DEV, nonblind content and one learned seed; synthesis reuses authoritative ratings without new evaluations.')
    atomic_json(target,output)
    print(json.dumps(dict(status=output['status'],CPU_seconds=output['CPU_seconds'],conditions=len(rows),new_GPU_seconds=0)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
