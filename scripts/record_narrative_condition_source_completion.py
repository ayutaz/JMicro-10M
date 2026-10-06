"""Record the finite failed source branch; preserve all actual evidence."""
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
from narrative_condition_source import DATA, NarrativeTrainView
from prepare_narrative_condition_source import RUN, PROPOSAL, FREEZE, SOURCES


def ref(path): return dict(path=str(path), sha256=sha256(path))


def main():
    destination = ROOT / 'reports/phase6/narrative_condition_source_completion.json'
    if destination.exists(): raise ValueError('Preserve actual completion evidence')
    p = read_json(PROPOSAL); f = read_json(FREEZE); job = read_json(RUN / 'job.json')
    m = read_json(DATA / 'manifest.json'); review = read_json(DATA / 'content-review.json')
    if (job['status'] != 'complete_pending_fixed64_content' or alive(job) or job['CPU_seconds'] > 60
            or job['freeze_sha256'] != sha256(FREEZE) or f['source_sha256'] != {s: sha256(ROOT / s) for s in SOURCES}
            or not review['all64_read'] or review['training_pool_accepted']
            or review['weak_documents'] != 7 or review['unresolved_grammar_documents'] != 3
            or review['unresolved_grounding_documents'] != 1 or m['documents'] != 16384
            or review['manifest_sha256'] != sha256(DATA / 'manifest.json') or review['notes_sha256'] != sha256(DATA / 'content-notes.json')):
        raise ValueError('Actual terminal preparation/all64 rejected content/frozen inputs required')
    # The new loader must prevent the rejected source from reaching a GPU trainer.
    try: NarrativeTrainView(DATA, job['manifest_sha256'])
    except ValueError as error:
        if 'Accepted raw-bound fixed64' not in str(error): raise
    else: raise ValueError('Rejected source unexpectedly admitted')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model', timeout=10) as response: ui = json.load(response)
    if ui['checkpoint_sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290' or ui['busy']:
        raise ValueError('Original idle UI required')
    processes = []
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try: args = path.read_bytes().replace(b'\0', b' ').decode('utf-8')
        except (OSError, UnicodeDecodeError): continue
        if 'scripts/webui.py --port 7860' in args and '.venv/bin/python' in args:
            processes.append(identity(int(path.parent.name)))
    if len(processes) != 1 or not alive(processes[0]): raise ValueError('One live original UI identity required')
    next_action = ('Read only the accepted existing natural-story TRAIN manifest, provenance/content acceptance and completed '
                   'same-parent controls in a bounded CPU metadata review; define one nonduplicate source replacement comparison. '
                   'Do not repair/reroll this rejected narrative source or launch its100M. No new GPU until a separate source/protocol and actual CUDA/budget gates qualify.')
    completion = dict(status='fixed64_narrative_source_preparation_complete_rejected_no_student_training', created_at=now(),
        proposal=ref(PROPOSAL), freeze=ref(FREEZE), preparation=ref(ROOT / 'reports/phase6/narrative_condition_source_preparation.json'),
        manifest=ref(DATA / 'manifest.json'), pilot=ref(DATA / 'content-pilot.json'), notes=ref(DATA / 'content-notes.json'),
        review=ref(DATA / 'content-review.json'), job=job, source_sha256=f['source_sha256'], tests=f['tests'],
        documents=16384, TRAIN_fact_families=1024, new_independent_semantic_families=0,
        body_tokens=m['generated_body_tokens'], body_bytes=m['generated_body_bytes'], serialized_tokens=m['serialized_tokens'],
        body_plus_EOS_teachers_if_used=m['full_CE_targets'], EOS_tokens=m['EOS_targets'],
        body_length_min=m['body_length_min'], body_length_max=m['body_length_max'],
        all_whole_texts_unique=True, whole_document_exact_native_bytes=True, truncations=0, reserved_body_ids=0,
        source_CPU_seconds=job['CPU_seconds'], source_CPU_ceiling_seconds=60, fixed64_individually_read=True,
        weak_documents=7, maximum_weak_documents=10, weak_count_gate_passed=True,
        unresolved_grammar_documents=3, unresolved_grounding_documents=1, training_pool_accepted=False,
        rejected_source_admission_refused_by_native_loader=True,
        student_scientific_teacher_tokens=0, student_verification_teacher_tokens=0, student_optimizer_updates=0,
        GPU_seconds=0, related_GPU_seconds_preserved=p['preserved_related_GPU_seconds'],
        new_original_corpus_tokens=0, new_surface_source_tokens_prepared_but_not_used=m['serialized_tokens'],
        proposed100M_cancelled_at_content_prerequisite=True,
        interpretation='This renderer has unresolved expression/chronology issues, so the entire source fails its predeclared readiness gate. No model was trained; no conclusion about narrative-learning efficacy, capacity or unique root cause follows.',
        no_post_pilot_renderer_filter_reroll_or_content_corrections=True,
        independent_human_blind=False, protected_test_used=False,
        original_UI=ui, original_UI_identity=processes[0],
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        quality_criteria_unchanged=True, next_action=next_action)
    atomic_json(destination, completion)
    # Only small evidence/code: full generated source and arrays remain native.
    files = [PROPOSAL, FREEZE, destination, ROOT / 'reports/phase6/narrative_condition_source_tests.xml',
             ROOT / 'reports/phase6/narrative_condition_source_preparation.json',
             ROOT / 'reports/phase6/narrative_condition_source_content_review.json',
             *[ROOT / s for s in SOURCES], ROOT / 'scripts/freeze_narrative_condition_source.py',
             ROOT / 'scripts/record_narrative_condition_content_notes.py', Path(__file__),
             *[RUN / name for name in ('job.json', 'manifest.json', 'content-pilot.json', 'content-notes.json', 'content-review.json')]]
    archive = ROOT / 'reports/phase6/narrative_condition_source_evidence.tar.gz'
    if archive.exists(): raise ValueError('Preserve actual portable evidence')
    evidence = {path.relative_to(ROOT).as_posix(): dict(bytes=path.stat().st_size, sha256=sha256(path)) for path in files}
    with tarfile.open(archive, 'w:gz') as stream:
        for path in files: stream.add(path, arcname=path.relative_to(ROOT).as_posix(), recursive=False)
    atomic_json(ROOT / 'reports/phase6/narrative_condition_source_portable.json', dict(status='failed_fixed64_source_evidence_portable',
        files=evidence, file_count=len(evidence), raw_bytes=sum(v['bytes'] for v in evidence.values()), archive=ref(archive),
        full_source_and_arrays_preserved_native_only=str(DATA), no_model_tensors_created=True))
    prefix = f'''TRAIN由来の短文教材16384件を実準備・固定64全読解し不採用（2026-10-06 JST）。前診断・単一source案はdbdd9c5へ保存したprogress。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完成時に通知して停止。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

narrative_condition_source_freeze.jsonでproposal/accepted TRAIN input/owned renderer/prep/reviewer/test/seedをactual source生成前に凍結。既accepted1024facts/両branch/各8surfaceの全16384文、同48category×surfaceの固定48＋追加16の64を一度だけ準備。実CPU{job['CPU_seconds']:.6f}秒/上限60、body{m['generated_body_tokens']}、serialized{m['serialized_tokens']}、本文+EOS{m['full_CE_targets']}、EOS16384。native4096 exact bytes/BOS/EOS/wholebody入力1024内、重複全体文0/切捨て0/role-pad本文0。新独立semantic families/原文corpus0で、表現数増加を意味の独立例数・新公開自然文に置換しない。元24source formsは場面/関係/機構に残り、同surface内でも元formの違いがある。

CPU4tests/1.02秒で実TRAIN全coverage・ opposed状態/数量/時刻/人物/機構・native96 fixture codecと中途document再開・raw content改変拒否が成功。fixtureはactual内容レビューではない。固定64は全件個別に読みraw SHA/rationaleをcontent-notes/reviewへ保存、弱7/64でweak<=10は通るが未解消文法表現3・grounding時系列1のゼロ条件に失敗。causalityの重ねた主語2件、靴の非購入で退店前に「持ち帰ることはなかったのを見て」とする観測理由が問題。grammar旗は自然な文法表現の未解消で、全て形式的に構文解析不可能という証明ではない。全件nonblind Codex、人間/外部事実認証なし。

教材全体を不採用、実native loaderも拒否。凍結後renderer/pilot/selector修正・良い例だけ選択・rerollなし、提案100Mはcontent prerequisiteで取り消し、CUDA probe/学生科学・検証教師/optimizer/新GPUすべて0。失敗は今回の生成表現/時系列でありモデルの学習効果・容量限界・唯一原因を証明しない。既存強いstagedCE/absolute/歴史WebBPB guardの全基準を保持、過去関連GPU2289.596018秒も消さない。準備済みsource/tensorはnative/data、text/source/proposal/tests/全64は可搬archiveへ保存。

次は既存の採用済み自然物語TRAINのmanifest・provenance/content acceptanceと完了same-parent対照だけを有限CPUで確認し、過去と重複しない単一source置換比較を定義する。この不採用sourceは再試行しない。別source/protocolの準備・実CUDA4vs2+2/steady timings/予算gate前にGPUを開始しない。品質pilot合格時だけ独立学習seed/full dev/protected test/adoptionへ進む。科学GPUjob0、元10B UI{processes[0]['pid']}/boot{processes[0]['boot_id']}/start{processes[0]['start_ticks']}とHTTP親410f975d…/10000007168/busy=falseを確認。旧Phase0–3/数値7失敗を保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md', 'docs/15_project_roadmap.md', 'docs/windows_handoff.md'):
        path = ROOT / relative; path.write_text(prefix + path.read_text(encoding='utf-8-sig'), encoding='utf-8')
    progress_path = ROOT / 'reports/phase6/five_step_progress.json'; progress = read_json(progress_path)
    progress.update(status='Base_only_narrative_source_actual16384_fixed64_complete_rejected_GPU0', updated_at=now(),
        narrative_condition_source_completion=ref(destination), next_action=next_action,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False)
    atomic_json(progress_path, progress)
    print(json.dumps(dict(status=progress['status'], CPU_seconds=job['CPU_seconds'], source_accepted=False,
                         weak=7, grammar=3, grounding=1, new_student_GPU_seconds=0), ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
