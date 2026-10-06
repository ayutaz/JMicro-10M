"""Portable preparation/completion of the finite unchanged-CE TRAIN assay."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import argparse
import json
from pathlib import Path
import statistics
import sys
import tarfile
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,identity
from source_gradient_attribution import GROUPS
import diagnose_source_gradient_attribution as study


def original_UI():
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:ui=json.load(response)
    processes=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:args=path.read_bytes().replace(b'\0',b' ').decode('utf-8')
        except (OSError,UnicodeDecodeError):continue
        if 'scripts/webui.py --port 7860' in args and '.venv/bin/python' in args:processes.append(identity(int(path.parent.name)))
    if (len(processes)!=1 or not alive(processes[0]) or ui['busy']
            or ui['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'):
        raise ValueError('Original actual idle UI required')
    return dict(identity=processes[0],actual_alive_verified=True,HTTP=ui)


def summarize(records):
    groups={};pairs={}
    for name in (*GROUPS,'conditional_total','independent_total'):
        rows=[r['diagnostics']['groups'][name] for r in records];count=sum(r['teachers'] for r in rows)
        groups[name]=dict(teachers=count,teacher_fraction=count/sum(r['diagnostics']['total_teacher_count'] for r in records),
            teacher_weighted_CE=sum(r['CE_mean']*r['teachers'] for r in rows if r['teachers'])/count if count else None,
            median_contribution_gradient_norm=statistics.median(r['contribution_gradient_norm'] for r in rows),
            median_contribution_to_total_squared_norm=statistics.median(r['contribution_to_total_squared_norm'] for r in rows),
            median_group_mean_gradient_norm=statistics.median(r['group_mean_gradient_norm'] for r in rows if r['group_mean_gradient_norm'] is not None) if count else None)
    for name in records[0]['diagnostics']['pairs']:
        values=[r['diagnostics']['pairs'][name]['cosine'] for r in records if r['diagnostics']['pairs'][name]['cosine'] is not None]
        pairs[name]=dict(supported_batches=len(values),median_cosine=statistics.median(values) if values else None,
            minimum_cosine=min(values) if values else None,maximum_cosine=max(values) if values else None,negative_batches=sum(v<0 for v in values))
    return dict(groups=groups,pairs=pairs,maximum_decomposition_relative_L2_error=max(r['diagnostics']['decomposition_relative_L2_error'] for r in records))


def main(phase):
    c=study.inspect();ui=original_UI();destination=ROOT/f'reports/phase6/source_gradient_attribution_{phase}.json'
    if destination.exists():raise ValueError('Preserve original diagnostic milestone')
    report=dict(status='TRAIN_attribution_prepared_unstarted',created_at=now(),config=study.reference(study.CONFIG),
        CPU_preparation_seconds=c['CPU_preparation_seconds'],logical_batch=32,microbatch=8,context=1024,consecutive_TRAIN_batches_per_model=16,
        checkpoints=c['checkpoints'],samples_metadata=study.reference(study.RUN/'samples.json'),
        numerical_decomposition_relative_L2_tolerance=.02,GPU_ceiling_seconds=90,scientific_teacher_tokens=0,optimizer_updates=0,GPU_seconds=0,
        original_UI=ui,quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        next_action='Run the fixed two-endpoint TRAIN16 attribution once; no optimizer or new quality experiment.')
    prefix=f'''固定TRAIN16・二endpointの勾配寄与診断を実装・CPU準備完了（2026-10-06 JST）。Baseのみ継続し実完成時に通知/停止、Chat/Dialogue/SFT/量子化なし。

関連CPU3tests/0.85秒（tied parameter一回・不均一mask/分母・microbatch加算・逆向き勾配・zero support/null cosine・不変model/RNG・数値不一致/非有限値拒否）とPS構文成功。CPU準備{c['CPU_preparation_seconds']:.6f}秒/上限30、元mixedの先頭16同TRAIN input/reference digest/実masked target digest/source routes/会計が実旧historyと一致。217MB cache再利用・全source再scanなし。original10.5B親と前失敗終端を品質選別せず固定、logical32/context1024を8系列ずつ計算し、同logical全実教師分母でFP32 parameter gradientsを加算する。nativeBF16/math・unique tied parameter・元token-mean CE、5target group和と独立元CE勾配の相対L2誤差<=.02を全model/batchに事前固定。数値基準を品質基準と混同しない。新GPU/optimizer/学習教師0、configs/phase6/source_gradient_attribution.json凍結・未起動、全GPU上限90秒。

元10B UI{ui['identity']['pid']}をactual ps/HTTP親410f975d…/busy=falseで確認。次はscripts/diagnose_source_gradient_attribution.ps1で永続read-only起動→全32point/不変weights・gradなし/eval/finite/RNG/数値分解一致/実終端/UI/可搬証拠/commit。前第四条件は0c81347へ不採用保存、Base採用/独立学習seed/full dev/protected test未達。勾配は局所観測で品質や原因・重み変更の自動推奨ではない。凍結旧source/Phase0–3/数値7失敗/全品質基準保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    if phase=='completion':
        job=read_json(study.RUN/'job.json');r=read_json(study.RUN/'result.json');metadata=read_json(study.RUN/'samples.json')
        if (job['status']!='complete' or alive(job) or r['config_sha256']!=sha256(study.CONFIG)
                or job['GPU_seconds']!=r['GPU_seconds'] or r['GPU_seconds']>90 or not r['RNG_restored']
                or r['optimizer_updates'] or r['new_teacher_tokens'] or set(r['models'])!=set(c['checkpoints'])):
            raise ValueError('Actually terminal read-only bounded diagnostic required')
        summaries={}
        for arm,model in r['models'].items():
            if len(model['records'])!=16 or model['checkpoint']!=c['checkpoints'][arm] or not all(model['read_only_checks'].values()):
                raise ValueError('Full unchanged learned-model diagnostic required')
            for i,record in enumerate(model['records']):
                d=record['diagnostics']
                if (record['input']!=metadata['rows'][i] or record['checkpoint']!=c['checkpoints'][arm] or record['config_sha256']!=sha256(study.CONFIG)
                        or d['total_teacher_count']!=metadata['rows'][i]['teachers'] or d['unique_parameter_elements']!=10001152
                        or d['decomposition_relative_L2_error']>.02 or d['decomposition_tolerance']!=.02
                        or {g:d['groups'][g]['teachers'] for g in GROUPS}!=metadata['rows'][i]['teachers_by_group']):
                    raise ValueError('All fixed actual input/count/vector/decomposition points required')
            summaries[arm]=summarize(model['records'])
        previous=read_json(ROOT/'reports/phase6/interleaved_outcome_completion.json')['related_GPU_seconds']
        report.update(status='fixed_TRAIN_gradient_attribution_complete_Base_unfinished',result=study.reference(study.RUN/'result.json'),
            actual_terminal_job=job,actual_process_absent=True,GPU_seconds=r['GPU_seconds'],read_only_checks={a:m['read_only_checks'] for a,m in r['models'].items()},
            RNG_restored=True,summaries=summaries,gradient_teacher_targets_per_model=r['gradient_teacher_targets_per_model'],
            distinct_TRAIN_input_tokens=r['distinct_logical_input_tokens'],previous_related_GPU_seconds_preserved=previous,related_GPU_seconds=previous+r['GPU_seconds'],
            limitations=r['limitations'],next_action='Interpret fixed TRAIN gradient evidence with completed four-cell comparison; define one distinct Base intervention with fixed comparison/budget and unchanged quality gates before further learning.')
        brief=json.dumps({a:dict(conditional_TEACHER_fraction=s['groups']['conditional_total']['teacher_fraction'],
            conditional_gradient_total_squared_norm_contribution=s['groups']['conditional_total']['median_contribution_to_total_squared_norm'],
            Web_conditional_median_cosine=s['pairs']['web__conditional_total']['median_cosine'],
            maximum_decomposition_relative_L2_error=s['maximum_decomposition_relative_L2_error']) for a,s in summaries.items()},ensure_ascii=False)
        prefix=f'''固定TRAIN16・二endpointのread-only勾配寄与診断を実完了（2026-10-06 JST）。Base未完了、完成時に通知/停止、Chat/Dialogue/SFT/量子化なし。

actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}はcomplete・実不在。元10.5B親と前mask/mixed終端で全16同TRAIN batch/context1024/logical32を固定micro8で測定、unique10001152paramを一回、実勾配target{r['gradient_teacher_targets_per_model']}/model・distinct input524288。optimizer/新学習教師0。全32pointの5source-target group和と独立token-mean CEの相対L2誤差<=.02、全不変weights/gradなし/eval/finite/RNG checks成功。GPU{r['GPU_seconds']:.6f}秒/上限90。局所記述値: {brief}

source_gradient_attribution_completion/portable/archiveへraw points/実会計/PID/コード/tests/config/数値分解を保存。元10B UI{ui['identity']['pid']}/boot{ui['identity']['boot_id']}/start{ui['identity']['start_ticks']}はactual ps/HTTP親410f975d…/busy=false。関連series累積{report['related_GPU_seconds']:.6f}秒（全project費用ではない）。勾配はこのTRAIN16/一学習seed/選定済二endpointの局所観測、optimizer方向/品質/因果/自動loss重み変更の証明ではない。元第四条件の不採用・全品質基準/旧失敗・Phase0–3/数値7失敗を保持、Base採用/独立seed/full dev/protected test未達。次はこの結果と既四条件から別機序の一つのBase介入を比較/予算付きで定義する。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PROPOSAL,study.TESTS,study.RUN/'samples.json',Path(__file__),*[ROOT/s for s in study.SOURCES]]
    if phase=='completion':files.extend(p for p in sorted(study.RUN.rglob('*.json')) if p.is_file())
    files=list(dict.fromkeys(files));evidence={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/f'reports/phase6/source_gradient_attribution_{phase}_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve original portable diagnostic evidence')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/f'reports/phase6/source_gradient_attribution_{phase}_portable.json',dict(files=evidence,file_count=len(files),
        raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=study.reference(archive),tensors_native_only=True))
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status=report['status'],updated_at=now(),next_action=report['next_action'],
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['source_gradient_attribution_'+phase]=study.reference(destination);atomic_json(progress_path,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=report['GPU_seconds'],portable_files=len(files)),ensure_ascii=False))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--phase',choices=('preparation','completion'),required=True);main(p.parse_args().phase)
