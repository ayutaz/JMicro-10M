"""Save one actual boundary assay and a predeclared fourth order/target cell."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import json
from pathlib import Path
import sys
import tarfile
import time
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,identity
from shared_prefix_web_loss import decompose
from run_eos_short_pilot import equal_state
import diagnose_shared_prefix_web_loss as study


def main():
    started=time.monotonic();c=study.inspect();r=read_json(study.RUN/'result.json');job=read_json(study.RUN/'job.json')
    destination=ROOT/'reports/phase6/shared_prefix_web_loss_completion.json'
    if destination.exists():raise ValueError('Preserve original single boundary diagnosis')
    bodies=read_json(study.RUN/'cached-bodies.json');bodies['shared_prefix']=read_json(study.RUN/'body.json')['body'];expected=decompose(bodies)
    if (job['status']!='complete' or alive(job) or job['GPU_seconds']!=r['GPU_seconds'] or r['GPU_seconds']>30
            or r['config_sha256']!=sha256(study.CONFIG) or not all(r['read_only_checks'].values())
            or not all(equal_state(r[k],v) for k,v in expected.items()) or not r['shared_prefix_already_exceeds_historical_guard']):
        raise ValueError('Actually completed finite read-only common256 decomposition required')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:ui=json.load(response)
    processes=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:args=path.read_bytes().replace(b'\0',b' ').decode('utf-8')
        except (OSError,UnicodeDecodeError):continue
        if 'scripts/webui.py --port 7860' in args and '.venv/bin/python' in args:processes.append(identity(int(path.parent.name)))
    if len(processes)!=1 or not alive(processes[0]) or ui['busy'] or ui['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290':
        raise ValueError('Original actual idle UI must be restored')
    mixed_config=ROOT/'configs/phase6/historical_parent_condition_comparison_v3.json';mixed=read_json(mixed_config)
    mixed_run=ROOT/'reports/phase6/historical-parent-condition-comparison-v3-20261006'
    mixed_result=mixed_run/'compare-result.json';mixed_job=read_json(mixed_run/'job.json')
    if mixed_job['status']!='complete' or alive(mixed_job):raise ValueError('Original mixed control must actually be terminal')
    mixed_ev=read_json(mixed_result)['evaluations']['historical_parent']
    mask_run=ROOT/'reports/phase6/conditional-prefix-mask-20261006';mask_review=read_json(mask_run/'review.json')
    actual=mask_review['accounting']['actual_source_accounting']
    reference_goals=dict(web=75000000,story=5000000,ordinary_textbook=10000000,conditional_textbook=10000000)
    full_actual=dict(reference_goals,conditional_textbook=actual['teachers']['conditional_textbook'])
    proposal=dict(status='defined_not_implemented_not_launched',created_at=now(),trigger=study.reference(study.RUN/'result.json'),
        question='With the same conditional outcome+EOS targets and same four source quotas, does the original interleaved order retain Web loss while preserving Japanese continuation quality?',
        motivation='Shared-prefix WebBPB already exceeds the historical guard, and the final masked suffix adds further loss. '
            'Existing unmasked interleaved control retains Web loss but failed generation. The missing order-by-target cell can test their interaction.',
        frozen_original_fullparent=mixed['parent'],original_mixed_config=study.reference(mixed_config),
        cells=dict(full_targets_interleaved=dict(result=study.reference(mixed_result),config=study.reference(mixed_config),
                cached_BPB=mixed_ev['body']['bpb']),
            full_targets_staged=dict(result=read_json(study.PROPOSAL)['cached_comparators']['strong_staged']),
            outcome_EOS_targets_staged=dict(result=read_json(study.PROPOSAL)['cached_comparators']['masked_suffix'],
                review=study.reference(mask_run/'review.json'),new_run=False),
            outcome_EOS_targets_interleaved=dict(new_run=True,still_unstarted=True)),
        candidate='From the same original10.5B fullstate, use the original mixed sampler min(reference_source_teachers/reference_goals) '
            'and existing source tie order. Continue actual Web cursor; seed42 short-source streams. Keep existing conditional focus body+EOS only. '
            'All other source labels, text, relative within-source order, mask, nominal quotas and actual LR0.00001 remain fixed. No aux loss, role labels or reheat.',
        reference_teacher_goals=reference_goals,original_nominal_reference_teachers=100000000,
        predicted_actual_hard_teachers=sum(full_actual.values()),predicted_actual_teachers_by_source=full_actual,
        accounting='The staged masked whole recipe reused shared-prefix89840363 labels plus its suffix1801392 labels. '
            'Interleaved candidate newly learns all91641755 actual labels from original parent. Report reused versus new exposure and GPU separately. '
            'Verify source content/order/EOS/input windows and masked target hashes per source against both original mixed stream and existing staged recipe. '
            'Global batch order differs by design; do not claim identical global token digest.',
        source_order_factor='Original progress-balanced interleaving versus original exhaust-Web/story/ordinary/conditional order; source ratios are unchanged.',
        content_target_factor='All original conditional targets versus its same fixed outcome+EOS targets. No mask/EOS coefficient or source variant.',
        accepted_data=dict(pool=mixed['pool'],positive_data=mixed['positive_data'],original_web=mixed['original_web'],accepted_compact_index=mixed['accepted_compact_index']),
        CPU_preparation_ceiling_seconds=60,probe_GPU_ceiling_seconds=120,total_new_GPU_ceiling_seconds=900,
        prerequisites='Implement owned mixed mask sampler/fullstate accounting/runner and meaningful CPU tests before CUDA. '
            'Reuse217MB compact cache, no full source scan/dedup. Verify actual continuous8 vs resumed4+4 with mixed sources and active mask, '
            'finite BF16 fullstate/optimizer/scheduler/RNG/cursors/digests/counters, own32 timings. '
            'Science estimate1.3x+save+evaluation150+50 plus all probe/failed GPU must fit900 before freeze.',
        evaluation='Reuse all three completed cell evaluations/notes unchanged. New cell gets same256 common body/Japanese192-331-1119/greedy80 individually read/bridge128-retention128. '
            'Report paired source-order differences within each target scope and their interaction; one learned seed/shared data/repeated dev is not independent causal proof.',
        mandatory_quality_guards='Preserve strong staged23+8 coherence/paired CI lower>0/EOS>=76/repetition<=2; all absolute/practical and historicalWebBPB<=0.9812859519097707. '
            'Report the observed masked-staged35/EOS79/rep1 comparison as well, without favorable rescoring or silent baseline substitution.',
        failure='End the one predeclared fourth cell on readiness/quality/budget failure. No order list, ratio, mask position, EOS weight, '
            'source text, checkpoint, LR or decoder sweep to rescue it. All old failed cells remain unadopted.',
        completion='Actual new cell/whole scientific teacher accounting/all80/full evaluation/four-cell comparison/terminal/UI/commit. '
            'Only a qualified recipe permits independent learned seed/full dev/protected test/adoption.',
        new_teacher_tokens_so_far=0,optimizer_updates_so_far=0,GPU_seconds_so_far=0,quality_criteria_unchanged=True,
        protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        next_action='Implement one original-interleaved order with fixed outcome+EOS targets as the missing four-cell recipe comparison; own gates and measured budget before science.')
    next_path=ROOT/'reports/phase6/interleaved_outcome_order_proposal.json'
    if next_path.exists():raise ValueError('Preserve original finite order interaction proposal')
    atomic_json(next_path,proposal)
    prefix_change=r['comparisons']['shared_prefix_minus_historical']['BPB_change'];total_change=r['comparisons']['masked_minus_historical']['BPB_change']
    report=dict(status='fixed_shared_prefix_loss_localization_complete_Base_unfinished',created_at=now(),result=study.reference(study.RUN/'result.json'),
        config=study.reference(study.CONFIG),actual_terminal_job=job,actual_process_absent=True,read_only_checks=r['read_only_checks'],
        BPB=r['BPB'],comparisons=r['comparisons'],preconditional_prefix_fraction_of_masked_total_BPBincrease=prefix_change/total_change,
        shared_prefix_already_exceeds_historical_guard=True,historical_guard_limit=r['historical_guard_limit'],
        scientific_teacher_tokens=0,optimizer_updates=0,GPU_seconds=r['GPU_seconds'],CPU_preparation_seconds=c['CPU_preparation_seconds'],
        previous_related_GPU_seconds_preserved=2926.5694972780763,related_GPU_seconds=2926.5694972780763+r['GPU_seconds'],
        original_UI=dict(identity=processes[0],actual_alive_verified=True,HTTP=ui),next_proposal=study.reference(next_path),next_action=proposal['next_action'],
        limitations=r['interpretation']+' Whole prefix contains75M Web/5M story/9840363 ordinary labels. '
            'It does not identify an individual source or prove a model-capacity ceiling. Cached old GPU scores were not rerun.',
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    report['CPU_completion_seconds']=time.monotonic()-started
    if report['CPU_completion_seconds']>10:raise TimeoutError('Completion10s exhausted')
    atomic_json(destination,report)
    files=[destination,next_path,study.CONFIG,study.PROPOSAL,Path(__file__),*[ROOT/p for p in study.SOURCES],ROOT/'reports/phase6/shared_prefix_web_loss_tests.xml']
    files.extend(p for p in sorted(study.RUN.rglob('*.json')) if 'source' not in p.relative_to(study.RUN).parts)
    files=list(dict.fromkeys(files));evidence={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/shared_prefix_web_loss_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve original read-only evidence archive')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/shared_prefix_web_loss_portable.json',dict(files=evidence,file_count=len(files),
        raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=study.reference(archive),tensors_native_only=True))
    prefix=f'''固定shared-prefix Web loss診断を実完了、学習順序×教師対象の未測定一条件を定義（2026-10-06 JST）。前mask全学習/80不採用は4a9d124。Baseのみ品質・独立学習seed/full dev/protected test/採用まで継続し実完成時に通知/停止、Chat/Dialogue/SFT/量子化なし。

actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}はcomplete・不在。固定CP323185一つだけに全256 full body122343/common472055byteのnativeBF16/mathを新評価、教師・optimizer0、GPU{r['GPU_seconds']:.6f}秒/上限30。weights不変/no gradients/eval/finite/RNG復元の全5checks成功。関連CPU3tests/0.10秒、実準備{c['CPU_preparation_seconds']:.6f}秒/上限10、既3model評価再利用・旧GPU再実行0。

歴史WebBPB.971570249→conditional教師0のshared prefix1.013622108→full-target staged1.133612866、masked suffix1.086812357。prefix差+.042051859/paired byte-weighted CI[.040278905,.043796689]、full suffix差+.119990758/CI[.116045128,.124765116]、mask suffix差+.073190249/CI[.069758141,.077377444]、全差で256/256増加。mask全Web悪化の約{100*prefix_change/total_change:.3f}%は既prefix側で観測され、mask前から歴史guard<=.981285952を超える。残159637普通文教師もsuffixに含むのでconditional単独原因とはしない。source順序/範囲/独立seedを変えていない局所観測で、個々sourceや10M容量限界の証明ではない。原mask採否・全品質基準はそのまま、旧Phase0–3/数値7失敗も保持。

全256paired差/原raw/actual PID/readonly/コード/tests/configをshared_prefix_web_loss_completion/portable.json/archiveへ保存。元10B UI{processes[0]['pid']}/boot{processes[0]['boot_id']}/start{processes[0]['start_ticks']}をactual ps/HTTP親410f975d…/10000007168/busy=falseで確認。関連series累積{report['related_GPU_seconds']:.6f}秒（全project費用ではない）。Base未採用/独立学習seed/full dev/protected test未実施。

次はinterleaved_outcome_order_proposal.jsonの未測定一条件。同元10.5B fullparent/実LR.00001、元mixed samplerのmin(reference source教師/quota)による混在順序を使い、conditionalの既outcome+EOS maskと全source比率75/5/10/10・source原文/相対stream順序を固定する。全target/mixed・全target/staged・mask/stagedの既3条件にmask/mixedだけを加え学習レシピ4条件で交互作用を調べる。旧mask比較は結果を変更せず終了、source比率/新素材/mask位置/係数/EOS/decoder/CP選別を追加しない。global順序は変わるがsource別同窓/元target/maskedtarget/cursor/会計をCPUで確認。whole mask recipeの実教師予測91641755（conditional1641755+他90000000）、元reference100Mをactualと混同せず旧shared-prefix/対照学習を新教師に加えない。

新mixed mask sampler/trainer/accounting/runnerとCPUtestsを先に実装、CPU準備60秒/GPUprobe120/新全900秒。own mixed8対4+4実mask/source保存再開・32timing・実測1.3×+save+評価150+50/all probe失敗込みを通してからscience凍結。new科学/検証/GPU0、未実装/未起動。全256/Japanese192-331-1119/80個別/bridge-ret128、元strong23+8/CI正/EOS76/反復2・absolute/歴史WebBPB全guardとmasked-staged35/EOS79/反復1の差を明示。qualified recipe後だけ独立学習seed/full dev/protected test/adoption、失敗は一条件で終了しsweep救済なし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_shared_prefix_retention_loss_localized_missing_order_target_cell_defined',updated_at=now(),
        shared_prefix_web_loss_completion=study.reference(destination),next_action=report['next_action'],Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=r['GPU_seconds'],BPB=r['BPB'],prefix_share=prefix_change/total_change,portable_files=len(files))))


if __name__=='__main__':main()
