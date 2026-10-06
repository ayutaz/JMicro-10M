"""Persist one actual fixed-history ablation; keep Base adoption separate."""
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
from run_eos_short_pilot import equal_state
from record_source_gradient_attribution import original_UI
from document_context_ablation import summarize
import diagnose_document_context_ablation as study


def main(phase):
    c=study.inspect();ui=original_UI();destination=ROOT/f'reports/phase6/document_context_ablation_{phase}.json'
    if destination.exists():raise ValueError('Preserve original context milestone')
    report=dict(status='document_history_ablation_prepared_unstarted',created_at=now(),config=study.reference(study.CONFIG),
        checkpoints=c['checkpoints'],CPU_preparation_seconds=c['CPU_preparation_seconds'],GPU_seconds=0,GPU_ceiling_seconds=30,
        logical_batch=32,microbatch=8,context=1024,batches_per_model=16,cached_reference=c['references']['cached_full_causal'],
        original_UI=ui,new_teacher_tokens=0,optimizer_updates=0,quality_criteria_unchanged=True,protected_test_used=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        next_action='Run the sole two-endpoint same-document attention ablation; reuse full-history CE, no optimizer or generation re-evaluation.')
    prefix=f'''文書間historyの固定ablationを実装・CPU準備完了（2026-10-06 JST）。Baseのみ継続/実完成時に通知・停止、Chat/Dialogue/SFT/量子化なし。

関連CPU3tests/0.84秒で先頭partial segment/BOSごとの正確なcausal境界、native full-causal path一致（atol/rtol1e-6）、実small modelの他文書変更/未来変更の非干渉・weights/RNG不変、異なる教師数の集計/marker/欠損・count改変拒否を確認。fixtureは学習品質の証明ではない。実準備{c['CPU_preparation_seconds']:.6f}秒/上限15、既TRAIN16/全32 cached model point/実masked targetsとsource教師数を再利用、source scan0。configs/phase6/document_context_ablation.jsonを凍結、newGPU/optimizer/学習教師0、未起動、GPU全30秒。元10B UI{ui['identity']['pid']}をactual ps/HTTP親410f975d…/busy=falseで確認。

次はscripts/diagnose_document_context_ablation.ps1で永続起動→各model先頭8のnative対owned full-causal BF16/math control一致（atol.02/rtol.002固定、失敗なら終了）→全16同input/教師/絶対RoPE位置のsame-document causalのみ新評価→全32delta/局所marker/readonly/実終端/UI/可搬証拠/commit。終端conditional教師weighted CE増分>=.1natsかつ増分>=.1のbatch>=12/16が支持された場合のみ別の数値条件を両armで揃えたattention-policy学習比較を定義。未支持なら当packing仮説を学習せず終了。全品質基準/旧不採用/Phase0–3/数値7失敗維持、Base採用/独立seed/full dev/protected testは未達、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    if phase=='completion':
        r=read_json(study.RUN/'result.json');job=read_json(study.RUN/'job.json');metadata=read_json(Path(c['references']['metadata']['path']))
        if (job['status']!='complete' or alive(job) or r['config_sha256']!=sha256(study.CONFIG) or job['GPU_seconds']!=r['GPU_seconds']
                or r['GPU_seconds']>30 or not r['RNG_restored'] or r['optimizer_updates'] or r['new_teacher_tokens']
                or set(r['models'])!=set(c['checkpoints'])):raise ValueError('Actual finite completed read-only context assay required')
        summaries={}
        for arm,model in r['models'].items():
            control=model['control']
            if (model['checkpoint']!=c['checkpoints'][arm] or not all(model['read_only_checks'].values())
                    or not control['allclose'] or control['tolerance']!=c['control_tolerance'] or len(model['records'])!=16):
                raise ValueError('Native numeric control and complete unchanged model required')
            for i,point in enumerate(model['records']):
                if (point['input']!=metadata['rows'][i] or point['checkpoint']!=c['checkpoints'][arm] or point['index']!=i
                        or point['config_sha256']!=sha256(study.CONFIG) or point['cached_full_causal_result_sha256']!=c['references']['cached_full_causal']['sha256']):
                    raise ValueError('Every same-input actual point and reference required')
            summaries[arm]=summarize(model['records'])
            if not equal_state(summaries[arm],model['summary']):raise ValueError('Recorded full paired summaries differ')
        supported=summaries['completed_masked_mixed']['descriptive_conditional_history_dependence_marker']
        if supported!=r['completed_endpoint_history_dependence_marker']:raise ValueError('Predeclared marker differs')
        previous=read_json(ROOT/'reports/phase6/source_gradient_attribution_completion.json')['related_GPU_seconds']
        report.update(status='document_history_ablation_complete_local_marker_supported' if supported else 'document_history_ablation_complete_local_marker_unsupported',
            actual_terminal_job=job,actual_process_absent=True,result=study.reference(study.RUN/'result.json'),GPU_seconds=r['GPU_seconds'],
            summaries=summaries,native_controls={a:m['control'] for a,m in r['models'].items()},read_only_checks={a:m['read_only_checks'] for a,m in r['models'].items()},
            RNG_restored=True,completed_endpoint_history_dependence_marker=supported,
            previous_related_GPU_seconds_preserved=previous,related_GPU_seconds=previous+r['GPU_seconds'],next_action=r['next_action'],limitations=r['limitations'])
        brief=json.dumps({a:dict(conditional=s['groups']['conditional_total'],EOS=s['groups']['conditional_EOS'],
            marker=s['descriptive_conditional_history_dependence_marker']) for a,s in summaries.items()},ensure_ascii=False)
        prefix=f'''固定同TRAIN16の文書間history ablationを実完了（2026-10-06 JST）。Base未完了、実完成時に通知・停止、Chat/Dialogue/SFT/量子化なし。

actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}はcomplete・実不在。元10.5B親と前mask/mixed終端で各16同input/実masked教師/絶対RoPE位置を固定し、same-document causal attentionのみ新評価。全32既full-causal CEは再利用、各先頭8のowned対native BF16/math control一致、全weights不変/gradなし/eval/finite/RNG成功。GPU{r['GPU_seconds']:.6f}秒/上限30、optimizer/新学習教師0。局所TRAIN記述: {brief}

事前終端history依存markerは{supported}（conditional教師weighted CE増分>=.1かつ増分>=.1のbatch>=12/16）。この固定TRAIN/単一学習seed・cache再利用の局所観測で自然生成改善の証明ではない。次の具体分岐: {r['next_action']}。当診断のinput/CP/ratio/mask/source/tolerance/decoder sweepなし、旧全不採用と全品質基準維持。raw points/control/会計/PID/source/tests/configはdocument_context_ablation_completion/portable/archiveへ保存、tensorはnative。元10B UI{ui['identity']['pid']}/boot{ui['identity']['boot_id']}/start{ui['identity']['start_ticks']}をactual ps/HTTP親410f975d…/busy=falseで確認、関連series累積{report['related_GPU_seconds']:.6f}秒（全project費用ではない）。Base採用/独立seed/full dev/protected test未達、Phase0–3/数値7失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PROPOSAL,study.TESTS,Path(__file__),*[ROOT/s for s in study.SOURCES]]
    if phase=='completion':files.extend(p for p in sorted(study.RUN.rglob('*.json')) if p.is_file())
    files=list(dict.fromkeys(files));evidence={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/f'reports/phase6/document_context_ablation_{phase}_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve original document history evidence')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/f'reports/phase6/document_context_ablation_{phase}_portable.json',dict(files=evidence,file_count=len(files),
        raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=study.reference(archive),tensors_native_only=True))
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status=report['status'],updated_at=now(),next_action=report['next_action'],
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['document_context_ablation_'+phase]=study.reference(destination);atomic_json(progress_path,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=report['GPU_seconds'],portable_files=len(files)),ensure_ascii=False))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--phase',choices=('preparation','completion'),required=True);main(p.parse_args().phase)
