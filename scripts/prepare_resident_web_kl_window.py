"""Prepare the exact cached-control Web prefix; no GPU, model or corpus reparse."""
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.experiment import ROOT,read_json,sha256
from jmicro.training import atomic_json
from jmicro.eos_pilot import TrainView
from historical_parent_condition_trainer import historical_web_cursor
from resident_web_window import build
import torch

CACHE=Path('/home/aihub_ubuntu/jmicro-data/phase6/web-kl-resident-window-20261006')


def main():
    c=read_json(ROOT/'configs/phase6/source_order_condition_comparison_v2.json')
    ref=c['parent']
    if sha256(Path(ref['path']))!=ref['sha256']:raise ValueError('Actual parent differs')
    parent=torch.load(ref['path'],map_location='cpu',weights_only=False)
    cursor=historical_web_cursor(parent)
    result_path=ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006/compare-result.json'
    result=read_json(result_path);record=result['checkpoints']['source_order']
    count=record['source_input_tokens']['web']//1024
    if count!=73421 or record['additional_supervised_tokens']!=100000000:raise ValueError('Exact cached100M Web prefix required')
    view=TrainView(c['original_web']['path'],c['original_web']['manifest_sha256'])
    data=build(view,cursor,count,CACHE,workers=8,budget=180)
    report=ROOT/'reports/phase6/web_kl_resident_window_preparation.json'
    if report.exists():raise ValueError('Preserve existing preparation report')
    atomic_json(report,dict(status='exact_parent_Web_window_cached_GPU_not_started',cache_directory=str(CACHE),cache=data,
        parent=ref,cached_control_result=dict(path=str(result_path),sha256=sha256(result_path)),
        source_sha256={p:sha256(ROOT/p) for p in ('scripts/resident_web_window.py','scripts/prepare_resident_web_kl_window.py','tests/test_resident_web_window.py')},
        cached_input_slots=count*1025,cache_is_duplicate_original_train_IDs=True,newly_prepared_source_tokens=0,
        actual_GPU_seconds=0,scientific_teacher_tokens=0,quality_criteria_unchanged=True,Base_complete=False,
        next_action='Version loader-only trainer/runner for resident windows; preserve every main/reference target/cursor, KL math and900-second cumulative GPU ceiling including prior8.727 failed/30.861 successful verification. Measure actual combined CUDA timing again before100M science.'))
    print(dict(windows=count,cache_bytes=data['files']['windows.bin']['bytes'],CPU_seconds=data['CPU_elapsed_seconds'],GPU_seconds=0))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
