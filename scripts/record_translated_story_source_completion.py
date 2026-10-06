"""Preserve the terminal source decision and portable evidence; never train it."""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
import json
from pathlib import Path
import sys
import tarfile
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive, identity
from prepare_translated_story_source import RUN, PROPOSAL, FREEZE, SOURCES
from translated_story_source import TranslatedStoryTrainView


def reference(path):
    return dict(path=str(path), sha256=sha256(path))


def main():
    destination = ROOT / 'reports/phase6/translated_story_source_completion.json'
    archive = ROOT / 'reports/phase6/translated_story_source_evidence.tar.gz'
    if destination.exists() or archive.exists():
        raise ValueError('Preserve terminal source evidence')
    job = read_json(RUN / 'job.json'); manifest = read_json(RUN / 'manifest.json')
    freeze = read_json(FREEZE); review = read_json(RUN / 'content-review.json')
    if (job['status'] != 'complete_pending_fixed64_content' or alive(job)
            or job['CPU_seconds'] > job['CPU_ceiling_seconds']
            or job['manifest_sha256'] != sha256(RUN / 'manifest.json')
            or job['freeze_sha256'] != sha256(FREEZE)
            or freeze['source_sha256'] != {s: sha256(ROOT / s) for s in SOURCES}
            or not review['all64_read'] or review['training_pool_accepted']
            or review['weak_documents'] != 12 or review['unresolved_grammar_documents'] != 6
            or review['unresolved_grounding_documents'] != 2
            or review['notes_sha256'] != sha256(RUN / 'content-notes.json')
            or review['pilot_sha256'] != sha256(RUN / 'content-pilot.json')):
        raise ValueError('Actual immutable terminal preparation and all64 rejection required')
    try:
        TranslatedStoryTrainView(RUN, job['manifest_sha256'])
    except ValueError as error:
        if 'Accepted raw-bound fixed64' not in str(error):
            raise
    else:
        raise ValueError('Rejected source unexpectedly admitted')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model', timeout=10) as response:
        ui = json.load(response)
    if ui['checkpoint_sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290' or ui['busy']:
        raise ValueError('Original idle UI required')
    processes = []
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:
            args = path.read_bytes().replace(b'\0', b' ').decode('utf-8')
        except (OSError, UnicodeDecodeError):
            continue
        if 'scripts/webui.py --port 7860' in args and '.venv/bin/python' in args:
            processes.append(identity(int(path.parent.name)))
    if len(processes) != 1 or not alive(processes[0]):
        raise ValueError('One original live UI identity required')
    next_action = (
        'Close the failed generated/mixed/translation replacement route. Read only existing completion/review metadata '
        'to consolidate the tested sources, model quality and unchanged acceptance failures into one finite gap table '
        'before defining any further Base experiment. No new corpus scans, source filters, teacher/prompt/model '
        'rerolls or GPU repetition; select a new intervention only with a distinct hypothesis, comparison and completion condition.')
    completion = dict(status='original_translation_source_fixed64_rejected_no_student_training', created_at=now(),
        proposal=reference(PROPOSAL), freeze=reference(FREEZE), job=job,
        manifest=reference(RUN / 'manifest.json'), pilot=reference(RUN / 'content-pilot.json'),
        notes=reference(RUN / 'content-notes.json'), review=reference(RUN / 'content-review.json'),
        tests=reference(ROOT / 'reports/phase6/translated_story_source_tests.xml'),
        source_sha256=freeze['source_sha256'],
        documents=manifest['documents'], serialized_tokens=manifest['serialized_tokens'],
        body_tokens=manifest['body_tokens'], body_plus_EOS_targets_if_used=manifest['full_CE_targets'],
        EOS_targets=manifest['EOS_targets'], body_length_min=manifest['body_length_min'],
        body_length_max=manifest['body_length_max'], index_bytes_read=manifest['index_bytes_read'],
        source_CPU_seconds=job['CPU_seconds'], source_CPU_ceiling_seconds=60,
        fixed64_individually_read=True, weak_documents=12, maximum_weak_documents=10,
        unresolved_grammar_documents=6, unresolved_grounding_documents=2,
        training_pool_accepted=False, rejected_source_admission_refused=True,
        source_or_selection_modified=False, proposed100M_cancelled_at_content_prerequisite=True,
        native_arrays_preserved=str(RUN / 'document-index.npz'), new_original_corpus_tokens=0,
        student_scientific_teacher_tokens=0, student_verification_teacher_tokens=0,
        student_optimizer_updates=0, GPU_seconds=0, related_GPU_seconds_preserved=2289.596018486074,
        interpretation='The earlier13 translations with zero grammar flags did not establish source-wide quality. '
            'This new fixed64 fails readiness; it provides no model training efficacy, capacity or unique-root-cause conclusion. '
            'Flags are nonblind judgments about Japanese expressions and internal subject/object connections, not formal proofs '
            'that every alternative reading is impossible. Fantasy, tragic endings and implicit actions are allowed.',
        original_UI=ui, original_UI_identity=processes[0], independent_human_blind=False,
        external_fact_certification=False, protected_test_used=False, quality_criteria_unchanged=True,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        next_action=next_action)
    atomic_json(destination, completion)
    files = [PROPOSAL, FREEZE, destination, ROOT / 'reports/phase6/translated_story_source_tests.xml',
        ROOT / 'reports/phase6/translated_story_source_content_review.json',
        *[RUN / name for name in ('job.json', 'manifest.json', 'content-pilot.json', 'content-notes.json', 'content-review.json')],
        *[ROOT / s for s in SOURCES], ROOT / 'scripts/freeze_translated_story_source.py',
        ROOT / 'scripts/record_translated_story_content_notes.py', Path(__file__)]
    evidence = {p.relative_to(ROOT).as_posix(): dict(bytes=p.stat().st_size, sha256=sha256(p)) for p in files}
    with tarfile.open(archive, 'w:gz') as stream:
        for path in files:
            stream.add(path, arcname=path.relative_to(ROOT).as_posix(), recursive=False)
    atomic_json(ROOT / 'reports/phase6/translated_story_source_portable.json', dict(
        status='rejected_original_translation_fixed64_evidence_portable', files=evidence,
        file_count=len(evidence), raw_bytes=sum(v['bytes'] for v in evidence.values()),
        archive=reference(archive), full_corpus_and_arrays_not_copied=True))
    prefix = f'''既存TinyStories-JA翻訳源の固定64を全確認し、今回の置換比較を不採用（2026-10-06 JST）。Baseだけを完成時に通知して停止する境界を維持。Base未完了・未採用、Chat/Dialogue/SFT/量子化は未開始。

凍結proposal/source/seed2026100693/calibration除外から、既存TRAIN追加区間のwhole499066文書を本文変更・再encode・新取得なしで読み出した。serialized140036743/body139038611/本文+EOS139537677、長さ44–512。実CPU{job['CPU_seconds']:.6f}秒/上限60、535MB元indexは1200995bytesのみ部分読み。関連CPU3tests/0.76秒で境界・codec・途中文書とepoch再開・固定除外を確認。固定64は個別rawSHA/rationale付きで全読解し、weak12（上限10）/未解消日本語表現6/所有・主体接続2で内容基準未達。めかしめ、パパとうさぎ、バジーを言い返す、店の絵の具を自分の所有物扱い、父が閉めたドアを姉妹の行動へ置き換える等を記録。幻想・悲劇・省略・未使用の属性は自動失敗にしない。非blind Codex判定で独立人手/外部事実保証なし。

rejected sourceはnative loaderも拒否し、提案100M/CUDA probeは内容前提で取り消した。新科学/検証教師・optimizer/GPUすべて0。凍結後の本文修正/selector変更/reroll/別translation filterでの救済なし。前の13翻訳例の表現0からsource全体の品質を保証できなかった結果で、モデル学習効果や容量限界を示さない。全旧採否/Phase0–3/数値7失敗と関連GPU2289.596018秒は保持。completion/review/全64/code/testsをtranslated_story_source_portable.jsonのraw SHA付きarchiveへ保存、全corpusとcompact arrayはWSL側に保持。元10B UI{processes[0]['pid']}をactual identity/HTTP親410f975d…/busy=falseで確認。

次は既存の完了・採否metadataだけで、今回終了した生成/混合/翻訳source置換と完了したモデル比較の未達項目を一つの有限表へ整理する。追加の全量照合・source選別・同実験GPU反復は行わない。別のBase介入は未検証の仮説・比較・終了条件が定義できた場合だけ実装する。既存品質基準を維持し、合格pilot後の独立学習seed/full dev/protected test/採用まで完了としない。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md', 'docs/15_project_roadmap.md', 'docs/windows_handoff.md'):
        path = ROOT / relative
        path.write_text(prefix + path.read_text(encoding='utf-8-sig'), encoding='utf-8')
    progress_path = ROOT / 'reports/phase6/five_step_progress.json'
    progress = read_json(progress_path)
    progress.update(status='Base_only_translation_fixed64_rejected_source_route_closed', updated_at=now(),
        translated_story_source_completion=reference(destination), next_action=next_action,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False)
    atomic_json(progress_path, progress)
    print(json.dumps(dict(status=progress['status'], source_accepted=False,
                          weak=12, grammar=6, grounding=2, new_GPU_seconds=0)))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
