"""Persist actual masked CUDA evidence and measured suffix budget before science."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import json
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
import run_conditional_prefix_mask as study


def main():
    c=study.inspect(study.CONFIG);r=study.probe_evidence();job=read_json(study.RUN/'probe/job.json')
    destination=ROOT/'reports/phase6/conditional_prefix_mask_preparation.json'
    if destination.exists():raise ValueError('Preserve original actual preparation')
    report=dict(status='actual_masked_CUDA_resume_timing_complete_science_frozen_unstarted',created_at=now(),
        config=study.reference(study.CONFIG),probe_config=study.reference(study.PROBE_CONFIG),
        probe_result=study.reference(study.RUN/'probe/result.json'),actual_probe_job=job,actual_probe_process_absent=True,
        initial_fullstate_preservation=r['initial_fullstate_preservation'],resume_checks=r['gate']['checks'],
        verification_optimizer_updates=48,verification_teacher_tokens=r['verification_teacher_tokens'],verification_input_tokens=48*1024*32,
        scientific_teacher_tokens=0,scientific_optimizer_updates=0,GPU_seconds=r['GPU_seconds'],
        previous_related_GPU_seconds_preserved=2858.8479238640863,related_GPU_seconds=2858.8479238640863+r['GPU_seconds'],
        CPU_preparation_seconds=c['CPU_preparation_seconds'],remaining_updates=318,
        predicted_actual_masked_teachers=c['actual_scientific_teacher_tokens_predicted'],
        original_reference_suffix_teachers=c['reference_suffix_teacher_tokens'],remaining_physical_input_tokens=318*1024*32,
        reference_input_ledger=c['references']['reference_input_ledger'],own_measured_timing=c['measured_timing'],
        estimated_science_GPU_seconds_with_margin=c['estimated_GPU_seconds_with_margin'],total_GPU_ceiling_seconds=600,
        original_control100M_reused_not_new=True,matched_teacher_budget=False,
        initial_CPU_failure=dict(xml=study.reference(ROOT/'reports/phase6/conditional_prefix_mask_tests_initial_failure.xml'),
            failures=1,reason='Test fixture had no terminal padding; increased its test-only terminal batch to guarantee padding. '
                'Three tests then passed including zero-focus conditional EOS retention. No GPU before passes.'),
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        next_action='Launch durable same-input suffix318 updates; full256 common bytes/Japanese192-331-1119/greedy80/bridge-ret128; '
            'all80 individually read and compare all original guards. Qualified pilot alone permits independent seed/full dev/protected test/adoption.')
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PROBE_CONFIG,study.PROPOSAL,study.LEDGER,Path(__file__),*[ROOT/p for p in study.SOURCES],
        ROOT/'reports/phase6/conditional_prefix_mask_tests.xml',ROOT/'reports/phase6/conditional_prefix_mask_tests_initial_failure.xml']
    files.extend(p for p in (study.RUN/'probe').rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl') and 'source' not in p.relative_to(study.RUN).parts)
    files=list(dict.fromkeys(files));evidence={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/conditional_prefix_mask_preparation_evidence.tar.gz'
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/conditional_prefix_mask_preparation_portable.json',dict(files=evidence,file_count=len(files),
        raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=study.reference(archive),tensors_native_only=True))
    prefix=f'''条件prefix maskのown実CUDA保存再開/速度測定を完了、同入力suffix設定を凍結（2026-10-06 JST）。Baseのみを完成まで継続し通知して停止、Chat/Dialogue/SFT/量子化なし。

actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}はcomplete・不在。元CP323185のmodel/Adam/scheduler/RNG/全stream・source会計/cursor/実LR.00001が初期一致、実CUDA8対4+4でordinary→conditional切替と実mask更新を含む全state/history/有限値が一致。own32timing中央値{c['measured_timing']['steady_step_seconds']:.6f}秒、検証48更新/{r['verification_teacher_tokens']}教師/1572864inputを科学と別記。probe実GPU{r['GPU_seconds']:.6f}秒/上限120。CPU3tests/1.65秒・実準備2.868702秒/元残318全input/reference target digest一致、初回fixture padding1failed XMLも保持。新source/full index scanなし。

科学suffixは元source-order CP323185→323503の同318更新/physical10420224、reference quota教師10159637に対しmask後教師1801392を予測。元75M Web→5M story→10M ordinary→10M conditionalの先行学習/対照100Mを再利用するので新100M教師・同教師比較と称さない。conditional setup bodyだけをhardCEから外し既存outcome+EOSを保持、他source/input/順序/fullstate/LR不変。configs/phase6/conditional_prefix_mask.json SHA{sha256(study.CONFIG)}。train実測予測18.403642秒に1.3×/save/評価reserve150/余裕50を含みscience{c['estimated_GPU_seconds_with_margin']:.6f}秒、probe込み600秒以内。本学習まだ未開始。raw gates/timing/counters/failure/source/testをpreparation/portable.json/archiveへ保存。

次はscripts/run_conditional_prefix_mask.ps1 -Mode Trainで永続起動→同256common bytes・全日本語192-331-1119・greedy80個別raw/bridge-ret128→元strong/絶対/歴史WebBPBなど全guardで採否→元UI/可搬証拠/commit。失敗時にmask位置/EOS weight/source/checkpoint/decoder sweepで救済しない。qualified pilot後だけ独立学習seed/full dev/protected test/adoption、Baseまだ未完了。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_conditional_prefix_mask_own_CUDA_complete_science_frozen_unstarted',updated_at=now(),
        conditional_prefix_mask_preparation=study.reference(destination),next_action=report['next_action'],Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=r['GPU_seconds'],actual_masked_teachers_predicted=c['actual_scientific_teacher_tokens_predicted'],portable_files=len(files))))


if __name__=='__main__':main()
