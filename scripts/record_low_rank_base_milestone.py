"""Record actual Base-only preparation/probe/launch milestones and sources."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import argparse
import json
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import run_low_rank_base_comparison as study


def main(phase):
    destination=ROOT/f'reports/phase6/low_rank_base_v2_{phase}.json'
    if destination.exists():raise ValueError('Preserve original low-rank milestone')
    running=phase in ('launch','running')
    config=study.CONFIG if running else study.PROBE_CONFIG
    c=study.inspect(config) if not running else read_json(config)
    report=dict(status='fixed_rank4_Base_'+phase,created_at=now(),config=study.reference(config),
        actual_scientific_teacher_tokens_per_arm=91641755,nominal_reference_teachers_per_arm=100000000,
        new_scientific_teacher_tokens=0,GPU_seconds=0,GPU_ceiling_seconds=1800,probe_ceiling_seconds=240,
        native_parameters=10001152,rank4_trainable_parameters=232960,temporary_training_parameters=10234112,
        optimizer_policy='fresh_Adam_both_arms',quality_criteria_unchanged=True,protected_test_used=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    detail=f'''CPU4tests/1.65秒でzero-B初期native出力一致、私有初期化RNG、実勾配/frozen W0、数学的merge/native tied keys/params、両fresh-Adam連続4対2+2全state一致・改変拒否を確認。最初のwrapper階層とfixture key参照の3失敗は修正し、成功結果を保存した。実CPU準備{c['CPU_preparation_seconds']:.6f}秒/上限30。完了済み3068 input/target/source ledgerと217MB compact cacheを再利用し、全corpus照合/再変換なし。newGPU/学習0。次はownCUDA両armの連続8対4+4/全state・有限値/32timing/nativeFP32mergeを240秒以内に実測し、検証＋両学習/評価予測が1800秒以内の場合のみ本比較を凍結する。'''
    if phase=='probe':
        r=study.probe_evidence();report.update(result=study.reference(study.RUN/'probe/result.json'),GPU_seconds=r['GPU_seconds'],
            verification_teacher_tokens=r['verification_teacher_tokens'],GPU_optimizer_updates=96,
            actual_probe_process_absent=True,original_UI=original_UI(),arms=r['arms'])
        timings,estimate=study.estimate_training(r)
        report.update(measured_timings=timings,estimated_science_GPU_seconds_with_margin=estimate)
        detail=f'''両armの実CUDA/BF16/Flash/compile連続8対4+4 fullstate/history/有限値/no-reheatと初期native/RNG/freshAdam/cursor/count全checks成功。各32timing後の実FP32/math merged native control（atol.0002/rtol.00002・固定4×1024 TRAIN）成功、元数値7失敗は維持。検証96更新/{r['verification_teacher_tokens']}教師は本科学から除外、実GPU{r['GPU_seconds']:.6f}秒/240。実測両3068更新/保存と評価余裕を含む予測{estimate:.6f}秒、合計予測{estimate+r['GPU_seconds']:.6f}/1800。実終端/ps不在と元10B UIを確認。本科学/品質はまだ未実施。次は実測予算でconfig凍結→同actual91,641,755各の本比較/全日本語/全160→旧全gate採否。'''
    elif running:
        job=read_json(study.RUN/'job.json')
        if not alive(job) or job['config_sha256']!=sha256(config):raise ValueError('Actual bound science process required')
        report.update(actual_job=job,actual_live_process=True,GPU_seconds=job['GPU_elapsed_seconds'],
            new_scientific_teacher_tokens=job.get('actual_teachers',0),
            teacher_count_scope='Current arm completed updates observed at heartbeat, not final total across both arms.',
            verification_GPU_seconds=c['verification_GPU_seconds'],
            remaining_science_GPU_ceiling_seconds=c['GPU_budget_seconds'],estimated_GPU_seconds_with_margin=c['estimated_GPU_seconds_with_margin'])
        if phase=='running':
            report['supersedes_reporting_defaults_of_launch']=study.reference(ROOT/'reports/phase6/low_rank_base_v2_launch.json')
            report['reporting_correction']='Original launch top-level GPU_seconds/new_scientific_teacher_tokens defaulted to0 despite actual_job containing positive live progress. Raw original record/archive retained; use this observed heartbeat, not those defaults.'
        detail=f'''実測で両科学configを凍結。actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}をps確認、永続job/log/完了更新のmerged native＋unmerged adapter/Adam/scheduler/RNG/sampler/教師・input/source会計を保存。本科学上限{c['GPU_budget_seconds']:.6f}秒、検証{c['verification_GPU_seconds']:.6f}秒と合計1800。元UIは科学中停止しfinallyで元final10Bへ復帰。両actual91,641,755教師/各100,532,224input、全160内容/日本語/256common-byteと全旧gateの採否は未完了。restartは実PID不在確認後 scripts/run_low_rank_base_comparison.ps1 -Mode Train -Worker。'''
    else:report['original_UI']=original_UI()
    prefix=f'''固定rank4 LoRAのBase比較: {phase}（2026-10-06 JST）。Baseのみ継続・実完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

文書間packing依存markerは不支持、sequence unlikelihoodは既2比較不採用で再実行しない。今回は元W0を固定してrank4/scale1/dropout0の全attention/MLP7projection×13層だけを学習し、full更新と比較する。一方だけAdamをリセットする交絡を避け、両方fresh AdamW/同hyperparams/元scheduler clockとpermanent floor/actualLR.00001を使う。旧親Adamはprovenanceとして保持し継承したと偽らない。元native10,001,152、rank4の学習232,960/一時10,234,112、統合後10,001,152でnative評価する。凍結backboneでもactive adapterのWeb性能維持は保証されず、soft L2/KL/平均重みと同じ仮説へ代入しない。[一次論文](https://arxiv.org/abs/2106.09685)は当10Mの成功証拠ではない。

{detail}

同元10.5B親/元Webcursor/seed42/入力/条件outcome+EOSmask/75-5-10-10 reference quota/decoderを維持、両actual91,641,755教師、100M referenceと区別する。旧inherited-Adam mixed/full staged/masked stagedは歴史参照として保存し新matched controlと称さない。strong23+8 coherence/pairedCI>0・EOS>=76/反復<=2、絶対grammar56/coh27/適切27/EOS37/反復<=18/errors0、歴史WebBPB<=.9812859519097707の旧全gateを維持。不合格でrank/module/scale/LR/source/mask/CP/decoder sweepなし。合格recipeだけ独立学習seed/full dev/protected test/採用へ進む。Base/最終採用未達、Phase0–3/旧数値7/全失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    atomic_json(destination,report)
    files=[destination,config,study.PROPOSAL,ROOT/'reports/phase6/low_rank_base_tests.xml',Path(__file__),*[ROOT/s for s in study.SOURCES]]
    if phase=='probe':files.extend(p for p in sorted((study.RUN/'probe').rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1'))
    if running:files.append(study.RUN/'job.json')
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files},
        file_count=len(files),archive=study.reference(archive),tensors_native_only=True))
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    p=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(p)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['low_rank_base_'+phase]=study.reference(destination);atomic_json(p,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=report['GPU_seconds'],portable_files=len(files)),ensure_ascii=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=('preparation','probe','launch','running'));main(parser.parse_args().phase)
