"""Record the real CUDA gate and running owned Base job; preserve portable probe evidence."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
from pathlib import Path
import sys
import json
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_anchored_context_outcome_comparison as study


def ref(path):return dict(path=str(path),sha256=sha256(path))


def main():
    c=read_json(study.CONFIG);probe=study.probe_evidence();job=read_json(study.RUN/'job.json')
    if not alive(job) or job['config_sha256']!=sha256(study.CONFIG):raise ValueError('Actual live owned science identity required')
    if job.get('teachers',0)<=0 or job.get('stage')!='training':raise ValueError('Actual completed scientific update required')
    files=[]
    for folder in (study.RUN/'probe',study.RUN/'source'):
        files.extend(p for p in folder.rglob('*') if p.is_file() and p.suffix in ('.py','.ps1','.json','.jsonl','.xml'))
    files.extend([study.CONFIG,study.PROBE_CONFIG,
        ROOT/'reports/phase6/anchored_context_outcome_preparation.json',
        ROOT/'reports/phase6/anchored_context_outcome_cpu_tests.xml',
        ROOT/'reports/phase6/anchored_context_outcome_comparison_tests.xml'])
    records=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(set(files))]
    archive=ROOT/'reports/phase6/anchored_context_outcome_launch_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve launch archive')
    with tarfile.open(archive,'w:gz') as bundle:
        for row in records:bundle.add(ROOT/row['path'],arcname=row['path'],recursive=False)
    portable=ROOT/'reports/phase6/anchored_context_outcome_launch_portable.json'
    atomic_json(portable,dict(status='terminal_CUDA_probe_and_frozen_sources_portable_not_scientific_completion',
        created_at=now(),archive=ref(archive),files=records,raw_bytes=sum(r['bytes'] for r in records),
        tensors_and_data_native_only=True,active_science_logs_excluded=True))
    launch=ROOT/'reports/phase6/anchored_context_outcome_launch.json'
    record=dict(status='actual_positive_anchor_CUDA58_checks_passed_scientific100M_running',created_at=now(),
        config=ref(study.CONFIG),probe_config=ref(study.PROBE_CONFIG),proposal=ref(study.PROPOSAL),
        preparation=ref(ROOT/'reports/phase6/anchored_context_outcome_preparation.json'),
        probe_result=ref(study.RUN/'probe/result.json'),probe_GPU_seconds=probe['GPU_seconds'],
        probe_full_state_checks=probe['gate']['checks'],initial_parent_checks=probe['initial_parent_preservation'],
        verification_optimizer_updates=probe['GPU_optimizer_updates'],verification_main_CE_teachers=probe['verification_teacher_tokens'],
        verification_positive_anchor_teachers=probe['verification_positive_anchor_teacher_tokens'],
        verification_ranking=probe['verification_ranking'],verification_not_scientific_learning=True,
        all32_main_Web_and_pair_input_protocols_match_completed_ranking=True,
        actual_process={k:job[k] for k in ('pid','boot_id','start_ticks')},last_verified_at=now(),
        completed_scientific_main_CE_teachers=job['teachers'],observed_combined_loss=job['loss'],
        source_teachers=job['source_teachers'],run=study.RUN.relative_to(ROOT).as_posix(),restart_command=job['restart_command'],
        measured_timing=c['measured_timing'],science_GPU_estimate_with_margin=c['estimated_GPU_seconds_with_margin'],
        all_new_GPU_estimate_with_margin=c['estimated_GPU_seconds_with_margin']+probe['GPU_seconds'],
        new_total_GPU_ceiling_seconds=study.CEILING,previous_related_study_GPU_seconds=c['previous_related_study_GPU_seconds'],
        science_expected_main_CE_teachers=study.TOTAL,science_expected_positive_anchor_teachers=73725,
        expected_combined_hard_teacher_positions=100073725,expected_combined_physical_input=131948544,
        new_original_corpus_tokens=0,extra_input_relative_to_completed_ranking=0,
        portable=ref(portable),Base_complete=False,Base_adopted=False,Chat_started=False,
        quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
        operational_failures=[dict(stage='CPU_prepare_probe_before_freeze',error="KeyError('fixed_primary')",GPU_seconds=0,
            repair='Read the actual committed fixed_main proposal field; no config had been written and no frozen source was edited.')],
        next_action='Finish the one100M science job, same full256/Japanese/all80 individual content/bridge128/retention128 and absolute gold/foil NLL, then unchanged strong quality gates; qualified pilot alone is not completed Base.')
    atomic_json(launch,record)
    prefix=f'''正解続きの生成確率を高める単一100M比較を実CUDA検証後に開始（2026-10-06 JST）。前のrelative-only100M/全評価不採用を44b092cへ保存。Baseだけを品質・独立学習seed/full dev/protected test/採用まで続け、実完成時に通知して停止。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

owned anchored_context_outcome loss/trainer/resident/runner/accountant/reviewer/durablePSを実装。元10.5B fullparent/Adam/scheduler/RNG/実LR.00001、main100M CEと4source順序、conditional WebKL8x1024、TRAIN pair8x256/全cursor/inputを維持。同paired logitsの正解bodyにだけ非EOS CE係数1を加え、ranking係数/温度1を保持。foil/prefix/pad/EOS3は新hard教師外、追加forward/新教材量0。正解73725位置が新hard教師、main込み100073725とrelational labels/parent probability mass/combined physical131948544を別計数する。

CPU4tests/{read_json(ROOT/'reports/phase6/anchored_context_outcome_preparation.json')['CPU_test_seconds']:.3f}秒は実tiny学習済重みで全state4対2+2/3samplers/new ledger/singleAdamstep、loss masks/directEOS勾配0/低gold確率でも相対ranking改善する例とcausal/padding経路を確認。scope/実TRAIN会計改変拒否2testsも合格、PS構文成功。新builderの初回newline-fragment拒否とCPU prepareのproposal key誤読を新unfrozen sourceで修正後に凍結、実GPU失敗0、旧frozen files/基準/予算変更なし。

probe actual{read_json(study.RUN/'probe/job.json')['pid']}はcomplete・実identity不在。実CUDA4対2+2全58state/history/有限値checksと初期parent10checks成功。40検証更新/mainCE{probe['verification_teacher_tokens']}/positivehard{probe['verification_positive_anchor_teacher_tokens']}/rank160labels81920paddedを科学へ加算しない。全32主/Web/pair入力・mask digest・親massが終了済rankingと一致、probeGPU{probe['GPU_seconds']:.6f}秒。更新median{c['measured_timing']['steady_step_seconds']:.9f}秒、3068更新train推定{c['measured_timing']['estimated_training_seconds']:.6f}秒。同150秒非学習枠/30%/50秒余裕を保持しscience{c['estimated_GPU_seconds_with_margin']:.6f}+probe={record['all_new_GPU_estimate_with_margin']:.6f}<900秒でscience凍結。旧関連{c['previous_related_study_GPU_seconds']:.6f}秒を消さず別記。

Windows durable worker33620、actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}をlive確認。主CE追加{job['teachers']}教師/loss{job['loss']}有限で100M学習中。RUN {record['run']}、configs/phase6/anchored_context_outcome_comparison.json/launch.jsonにPID/log/checkpoint/source snapshotsを保存。actual不在・valid completed-update checkpointのときだけ{job['restart_command']}で再開、二重GPUなし。GPU中の元10B UIは停止しwrapper finallyで元CPへ復帰する。probe/sourceの可搬{len(records)}text/{sum(r['bytes'] for r in records)}rawbytesとarchiveを保存、active科学log/model tensor/dataはportable外、launch metadataはarchive後の別記録。

次は同job終端→256全文472055bytes/122343bodytokens、日本語192-331-1119、全80greedy64と全80個別raw-bound内容、bridge/retention各128、絶対gold/foil NLLとmargin、全3068入力/新hard台帳の採否。mechanism対照は前ranking、品質対照は強い元stagedCE23+8/CI lower>0/EOS>=76/反復<=2と既存absolute/歴史WebBPB<=.981285952のまま。設定sweep/量だけの延長/有利CP探索/自動予算拡張なし。pilot品質合格時だけ独立学習seed/full dev/protected test/adoption。旧Phase0–3/数値7失敗/全品質条件/過去費用保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        path=ROOT/relative
        path.write_text(prefix+path.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_positive_anchor_CUDA58_checks_passed_100M_running',updated_at=now(),
        requested_scope='Latest user boundary: qualified Base only; notify and stop; Chat/quantization deferred',
        Base_complete=False,Chat_started=False,quantization_started=False,
        anchored_context_outcome_preparation=record['preparation'],anchored_context_outcome_launch=ref(launch),
        next_action=record['next_action'])
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=record['status'],actual=record['actual_process'],teachers=job['teachers'],portable_text_files=len(records))))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
