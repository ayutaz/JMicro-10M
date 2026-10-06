"""Preserve source rejection, finite ancestry and one provenance-based next contrast."""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
from pathlib import Path
import sys
import json
import tarfile
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import identity, alive
from prepare_natural_story_source import RUN, PROPOSAL


def reference(path): return dict(path=str(path), sha256=sha256(path))


def main():
    completion_path=ROOT/'reports/phase6/natural_story_source_completion.json'
    next_path=ROOT/'reports/phase6/translated_story_source_proposal.json'
    if completion_path.exists() or next_path.exists():raise ValueError('Preserve actual source completion and next contrast')
    p=read_json(PROPOSAL);m=read_json(RUN/'manifest.json');review=read_json(RUN/'content-review.json')
    original=read_json(RUN/'job.json');repair=read_json(RUN/'metadata-repair-v2.json')
    provenance_path=ROOT/'reports/phase6/natural_story_provenance_result.json';provenance=read_json(provenance_path)
    ancestry_path=ROOT/'reports/phase6/natural_story_ancestry_result.json';ancestry=read_json(ancestry_path)
    if (original['status']!='failed_preserve_fixed_or_partial' or alive(original) or alive(repair)
            or repair['status']!='complete_pending_fixed64_content' or repair['cumulative_CPU_seconds']>60
            or not repair['original64_bytes_unchanged'] or not review['all64_read'] or review['training_pool_accepted']
            or review['weak_documents']!=10 or review['unresolved_grammar_documents']!=4
            or review['manifest_sha256']!=sha256(RUN/'manifest.json') or review['notes_sha256']!=sha256(RUN/'content-notes.json')
            or m['pilot_sha256']!=sha256(RUN/'content-pilot.json') or provenance['recovered_records']!=64 or ancestry['recovered_records']!=64
            or provenance['CPU_elapsed_seconds']>10 or ancestry['CPU_elapsed_seconds']>10
            or ancestry['cohorts']!={'retained':dict(documents=51,weak=7,unresolved_grammar=4),'translation':dict(documents=13,weak=3,unresolved_grammar=0)}):
        raise ValueError('Terminal fixed source rejection, unchanged repair and all64 exact ancestry required')
    for s,digest in p['source_sha256'].items():
        if sha256(ROOT/s)!=digest:raise ValueError('Frozen original source differs')
    if sha256(ROOT/'scripts/complete_natural_story_source_preparation_v2.py')!=repair['source_sha256']:
        raise ValueError('Actual metadata-only repair differs')
    source=Path('/home/aihub_ubuntu/jmicro-data/phase6/dataset-expansion-20261005/shards')
    source_manifest=read_json(source/'manifest.json'); old=Path(source_manifest['binding']['original_pool']['pool'])
    old_manifest=read_json(old/'manifest.json')
    if (sha256(old/'manifest.json')!=source_manifest['binding']['original_pool']['manifest_sha256']
            or sha256(ROOT/'scripts/prepare_dataset_expansion.py')!=source_manifest['binding']['builder_sha256']):
        raise ValueError('Recorded copy-old-then-append-translation provenance differs')
    start=old_manifest['splits']['train']['tokens']; end=source_manifest['splits']['train']['tokens']
    next_proposal=dict(status='one_pinned_original_translation_TRAIN_source_comparison_proposed_not_prepared',created_at=now(),
        trigger=reference(ancestry_path), rejected_mixed_story_review=reference(RUN/'content-review.json'),
        evidence='All4 unresolved expressions in this fixed64 lie in51 retained SimpleStories rows;13 translation rows have3 weak but0 unresolved grammar. Small correlated nonblind observation motivates source-origin comparison, not proof of source-wide superiority.',
        source=dict(repository=source_manifest['binding']['source']['repository'],revision=source_manifest['binding']['source']['revision'],
            license=source_manifest['binding']['source']['license'],native_pool=str(source),manifest=reference(source/'manifest.json'),
            retained_original_pool=reference(old/'manifest.json'),frozen_copy_then_append_builder=reference(ROOT/'scripts/prepare_dataset_expansion.py'),
            native_translation_serialized_interval=[start,end],serialized_tokens=end-start,
            prospective_translation_documents=source_manifest['splits']['train']['documents']-old_manifest['splits']['train']['documents'],
            all_existing_selected_TRAIN_translation_records=True,source_rows_or_text_not_modified=True,new_corpus_tokens=0,
            original_raw_file_download_or_scan=False,giant_JSONL_index_rescan=False,
            origin_policy='Use the recorded contiguous addition from shibatch/TinyStories-JA only; do not filter by observed content, length, grammar or favorable examples. The failed mixed source remains rejected.'),
        preparation=dict(CPU_ceiling_seconds=60,seed=2026100693,full_input_limit_tokens=1024,
            fixed_content_documents=64,
            method='Owned mmap view of the fixed appended interval; derive BOS/body/EOS offsets once from existing native IDs, reuse original builder/split integrity. Use bounded sorted-index seeks for selected metadata; no huge JSONL parse or raw corpus encoding.',
            content_sampling='Uniform64 fixed draws among translation TRAIN records not previously inspected as content calibration; freeze exclusions from every linked source-content packet before drawing. No reroll/filter/repair after pilot.',
            inspected_calibration_sources=[reference(RUN/'content-pilot.json'),reference(source/'samples.json'),
                reference(ROOT/'reports/phase6/textbook_mixture_content_review.json')],
            content_gate='All64 individually read/rawSHA bound; weak<=10, unresolved grammatical-expression/object/time-grounding0. Preserve fantasies and plausible alternative stories; no external fact certification.',
            failure='Reject this source contrast if readiness fails; do not attempt another translation filter/length/template/source variant to salvage it.'),
        proposed_comparison=p['proposed_comparison'],
        distinction='Final conditional10M uses only this separately pinned original translation source, rather than failed generated narratives or mixed retained/translation source. Same historical10.5B full parent/LR.00001 and strong same-parent stagedCE control; prior story mixtures have different parents/schedules/material/quotas.',
        limitations='Translation of originally synthetic English stories, not original human Japanese or new independent semantic evidence. Source content/diversity/length/EOS density change together. Existing global near/site/author audit remains incomplete. Earlier root diagnostic72 already found translation semantic weaknesses; the13 grammar0 here do not erase those failures.',
        scientific_teacher_tokens=0,GPU_seconds=0,quality_criteria_unchanged=True,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        next_action='Implement own native translation-only view/fixed64 preparation and meaningful provenance/boundary/codec checks; freeze input/exclusion/selection before actual preparation. Only accepted source can advance to own actualCUDA4vs2+2/32 changed-source timings and900s measured100M comparison.')
    next_proposal['proposed_comparison']=dict(next_proposal['proposed_comparison'],
        final_slot='Replace conditional10M with all existing selected source-TRAIN TinyStories-JA translations, excluding retained SimpleStories origin')
    atomic_json(next_path,next_proposal)
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:ui=json.load(response)
    if ui['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290' or ui['busy']:
        raise ValueError('Original idle UI required')
    processes=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:args=path.read_bytes().replace(b'\0',b' ').decode()
        except (OSError,UnicodeDecodeError):continue
        if 'scripts/webui.py --port 7860' in args and '.venv/bin/python' in args:processes.append(identity(int(path.parent.name)))
    if len(processes)!=1 or not alive(processes[0]):raise ValueError('One original live UI identity required')
    completion=dict(status='mixed_original_story_fixed64_rejected_all64_ancestry_complete_next_origin_contrast_defined',created_at=now(),
        proposal=reference(PROPOSAL),manifest=reference(RUN/'manifest.json'),pilot=reference(RUN/'content-pilot.json'),
        notes=reference(RUN/'content-notes.json'),review=reference(RUN/'content-review.json'),
        original_failed_job=original,metadata_only_repair=repair,
        original64_selection_and_all_native_bytes_unchanged=True,source_CPU_seconds_including_failed_v1=repair['cumulative_CPU_seconds'],
        source_CPU_ceiling_seconds=60,documents=m['documents'],body_tokens=m['body_tokens'],serialized_tokens=m['serialized_tokens'],
        body_plus_EOS_targets_if_used=m['body_plus_EOS_targets'],EOS_targets=m['EOS_targets'],
        body_length_min=m['body_length_min'],body_length_max=m['body_length_max'],
        fixed64_individually_read=True,weak_documents=10,maximum_weak_documents=10,weak_count_gate_passed=True,
        unresolved_grammar_documents=4,unresolved_grounding_documents=0,training_pool_accepted=False,
        full_story_corpus_quality_not_certified_by_old_mixed64=True,
        provenance=reference(provenance_path),ancestry=reference(ancestry_path),ancestry_cohorts=ancestry['cohorts'],
        index_bytes_read_total=provenance['index_bytes_read']+ancestry['index_bytes_read'],
        provenance_CPU_seconds=provenance['CPU_elapsed_seconds']+ancestry['CPU_elapsed_seconds'],
        byte_seek_tests=reference(ROOT/'reports/phase6/story_provenance_lookup_tests.xml'),
        original13GB_index_and536MB_index_not_fully_scanned=True,
        original_source_and_pilot_unchanged=True,source_acceptance_unchanged=True,
        proposed100M_and_GPU_probe_not_started=True,student_scientific_teacher_tokens=0,student_verification_teacher_tokens=0,
        student_optimizer_updates=0,GPU_seconds=0,related_GPU_seconds_preserved=2289.596018486074,
        next_source_proposal=reference(next_path),next_action=next_proposal['next_action'],
        interpretation='Source readiness failed before training, so there is no new model efficacy/capacity conclusion. Upstream cohorts motivate one separate pinned source-origin contrast, not a post-pilot repair of the failed mixed source.',
        source_authorship_clarification='The earlier proposal phrase independently authored means source text was not authored by this local renderer; it does not establish human or statistically independent authorship. Upstream material is public synthetic stories/translation.',
        original_UI=ui,original_UI_identity=processes[0],
        independent_human_blind=False,protected_test_used=False,quality_criteria_unchanged=True,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(completion_path,completion)
    files=[PROPOSAL,completion_path,next_path,*[RUN/name for name in ('job.json','metadata-repair-v2.json','manifest.json','content-pilot.json','content-notes.json','content-review.json')],
        ROOT/'reports/phase6/natural_story_source_content_review.json',provenance_path,ancestry_path,
        ROOT/'reports/phase6/natural_story_provenance_freeze.json',ROOT/'reports/phase6/natural_story_ancestry_freeze.json',
        ROOT/'reports/phase6/story_provenance_lookup_tests.xml',
        *[ROOT/s for s in ('scripts/prepare_natural_story_source.py','scripts/define_natural_story_source_reuse.py',
            'scripts/complete_natural_story_source_preparation_v2.py','scripts/review_natural_story_source.py',
            'scripts/story_provenance_lookup.py','tests/test_story_provenance_lookup.py',
            'scripts/audit_natural_story_provenance.py','scripts/audit_natural_story_ancestry.py')],Path(__file__)]
    evidence={v.relative_to(ROOT).as_posix():dict(bytes=v.stat().st_size,sha256=sha256(v)) for v in files}
    archive=ROOT/'reports/phase6/natural_story_source_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve original evidence archive')
    with tarfile.open(archive,'w:gz') as stream:
        for path in files:stream.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/natural_story_source_portable.json',dict(status='failed_mixed_story_source_all64_ancestry_portable',
        files=evidence,file_count=len(evidence),raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=reference(archive),
        source_corpora_and_model_arrays_not_copied=True))
    prefix=f'''既存物語100Mの固定64を全確認・不採用、全64の元sourceを小部分読みで確定（2026-10-06 JST）。前回の16384生成文/source失敗はfd48644に保存したprogress。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完成時に通知して停止。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

natural_story_source_reuse_proposal.jsonで別親/LR/素材の旧自然25M・storyweight100M・fresh教材量比較と、現在same10.5B staged条件源を比較し、最後のconditional10Mだけを既原文物語に置換する対照を定義。GPU起動前にTRAINの761448whole docs/serialized100000968/body98478072/本文+EOS99239520を確認、長さ34–511で切断0。旧2B poolのaccepted manifest/217MB compact cacheを再利用し13GBindex/5.37GBraw再走査・再取得なし。new corpus0/元原文変更0で、新量の用意やモデル改善としない。

CPU準備v1は固定64を保存した後、記録関数名refとループ変数の衝突TypeErrorで失敗。old metadata Windows-only2filesを正確SHA付きでWSLへ復元した初回定義失敗も隠さない。frozen v1/job/pilotを変えずowned metadata-repair-v2を用い、元draw64 IDs/text/token SHA完全一致で記録だけ完成。失敗+repair CPU{repair['cumulative_CPU_seconds']:.6f}秒/上限60、GPU0。actual64は全件読解/rawSHA/rationaleを保存、weak10で件数は通るが未解消表現4（ひとつの風/一番の素敵/むすんでいるように見えた太郎/ぎくりとした音）がゼロ条件を満たさず全mixed-story source不採用。grammar旗は自然な表現の未解消で、全て詩的読解が不可能という形式的証明ではない。幻想/暗い結末/新しい人物を自動失敗にせず、human/external truth認証なし。100M/GPU probe未実行。

source metadata探索をowned byte-seekで実装し、UTF8/最初・中間・末尾/欠損key/読出し上限のCPU2tests/.04秒成功。元13GB mixture JSONLと上流536MB JSONLから全64を2段のoffset二分探索で照合、実CPU{provenance['CPU_elapsed_seconds']:.6f}+{ancestry['CPU_elapsed_seconds']:.6f}秒（各上限10）、読出し{provenance['index_bytes_read']}+{ancestry['index_bytes_read']}={completion['index_bytes_read_total']}bytesのみ。全64本文SHA/bodytokens/TRAIN/source-family/元file-rowが一致。retained SimpleStories51件はweak7/表現4、translation13件はweak3/表現0。これは固定64の相関・非blind観察で元corpus全品質や因果を証明しない。旧root診断72の翻訳の意味失敗も消さない。

次はtranslated_story_source_proposal.jsonの別pinned source-origin比較。既shibatch/TinyStories-JA revision155b4e…のTRAIN追加区間{start}–{end}（serialized{end-start}、候補499066docs）だけのwhole native viewを用意する案。失敗mixed sourceの良い例だけを選別するのでなく、記録済copy-old-then-append builderで別公開sourceを全件再利用。原文/content/長さで再filterせずcalibration除外/seed2026100693/固定64/CPU60秒を生成前に凍結。新原文/GPU0、source原文・BOS/body/EOSからcompact offsetsを一度だけ導出し、536MBJSONLは64だけ部分読み。候補自身のweak<=10・grammar-grounding0に失敗ならこのorigin比較も終了、filter/length/source sweepで救済しない。

accepted sourceだけをsame fullparent/Adam/scheduler/RNG/実LR.00001、Web75M→story5M→ordinary10M→translation10M/ordinary CE1で強いstagedCE100Mに比較。first90M入力/cursors/counters一致を確認し、末尾source/EOS長さとall-masked Web padding差を正直に別会計。own changed-source実CUDA4vs2+2/32steady timings、150秒reserve/30%/50秒余裕・全probe込み900秒前に科学設定を凍結しない。全既存relative/absolute/歴史WebBPB guard・256full/Japanese192-331-1119/80個別/bridge-ret128維持。旧関連GPU2289.596018秒/Phase0–3/数値7失敗保持、科学GPUjob0、元10B UI{processes[0]['pid']}/boot{processes[0]['boot_id']}/start{processes[0]['start_ticks']}とHTTP親410f975d…/10000007168/busy=false確認。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        path=ROOT/relative;path.write_text(prefix+path.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_mixed_story64_rejected_all64_ancestry_complete_pinned_translation_contrast_proposed',updated_at=now(),
        natural_story_source_completion=reference(completion_path),translated_story_source_proposal=reference(next_path),
        next_action=next_proposal['next_action'],Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=progress['status'],source_accepted=False,cohorts=ancestry['cohorts'],new_GPU_seconds=0)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
