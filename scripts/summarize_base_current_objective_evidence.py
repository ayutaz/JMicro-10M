"""Keep four rejected studies and the never-trained KD budget distinction explicit."""
import json
import math
from pathlib import Path
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive


def ref(path): return dict(path=str(path),sha256=sha256(path))


def main():
    started=time.monotonic(); phase=ROOT/'reports/phase6'; output=phase/'base_current_objective_evidence.json'
    if output.exists(): raise ValueError('Preserve current evidence companion')
    rows=[]; control=None
    for key in ('on_policy_teacher','sam','middle_supervision','confidence_penalty'):
        path=phase/f'base_{key}_comparison_completion.json'; record=read_json(path)
        if (alive(record['actual_identity']) or record['scientific_CE_teacher_tokens']!=100000000 or
            record['eligible_for_final_Base_validation'] is not False or record['all80_individually_read'] is not True or
            any(record[k] is not False for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_scored'))):
            raise ValueError('Exited fully reviewed rejected original100M condition required')
        if control is None: control=record['summaries']['CE']
        elif control!=record['summaries']['CE']: raise ValueError('Historical matched CE changed')
        path_review=Path(record['review']['path'])
        if sha256(path_review)!=record['review']['sha256']: raise ValueError('Frozen review changed')
        review=read_json(path_review)
        rows.append(dict(condition=key,completion=ref(path),summary=record['summaries'][key],
            original_gold_positions=100000000,new_unique_corpus=0,matched_gates=review['matched_objective_quality'],
            GPU_seconds_including_probe=record['total_GPU_seconds_including_probe']))
    old_path=phase/'base_native_teacher_KD_probe_completion.json'; old=read_json(old_path)
    result_path=phase/'base-native-teacher-KD-probe-v2-20261007/result.json'; result=read_json(result_path)
    if (alive(old['actual_identity']) or old['science_started'] is not False or old['scientific_gold_positions']!=0 or
        old['prospective_total_GPU_cap_seconds']!=3600 or old['science_budget_eligible'] is not False or
        sha256(result_path)!=old['result_sha256'] or not all(old['actual_CUDA_checks'].values())):
        raise ValueError('Preserve actual never-trained native KD old-budget rejection')
    times=[row['seconds'] for row in result['histories']['timing'][3:]]
    if len(times)!=32 or any(not math.isfinite(t) or t<=0 for t in times): raise ValueError('Actual32 original timings required')
    forecast=math.ceil(17698/32*sum(times)*1.3+900)
    if time.monotonic()-started>30: raise TimeoutError('Evidence-only CPU30s cap')
    record=dict(created_at=now(),status='four_actual_quality_rejections_and_one_never_trained_KD_effect_distinguished',
        historical_synthesis=ref(phase/'base_failure_route_synthesis.json'),
        previous_companion=ref(phase/'base_recent_objective_failure_synthesis.json'),
        historical_files_overwritten=False,conditions=rows,cached_control=control,
        untrained_native_KD=dict(completion=ref(old_path),result=ref(result_path),scientific_gold_positions=0,
            old3600_budget_closed=True,old_median_based_forecast=old['scientific_forecast_seconds'],
            exact17698_mean32_forecast_seconds=forecast,mean32_step_seconds=sum(times)/32,
            actual_old_probe_seconds=old['cumulative_probe_GPU_seconds'],
            distinction='Finite CUDA/save-resume passed, science budget exceeded; no model-quality result exists for dense native gold-prefix KD. On-policy279734 distribution targets is a different context/amount and not this25M effect.'),
        next_action='A separately declared new prospective4800-total study of the same original eager native full-vocab short-prefix KD; explicit resource-plan reconsideration, not novel mathematics or retroactive old-budget success. Current implementation/state/teacher/source/budget gate before science; old3600 and failed compile/numeric results unchanged. No coefficient/teacher/decoder/source/parent tuning after result.',
        GPU_seconds=0,CPU_seconds=time.monotonic()-started,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_scored=False)
    atomic_json(output,record)
    print(json.dumps(dict(status=record['status'],conditions=len(rows),new_GPU_seconds=0,
                         previously_untrained_KD_mean_forecast=forecast)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
