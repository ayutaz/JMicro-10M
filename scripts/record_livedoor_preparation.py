"""Portable authored-news readiness and real shared-prefix evidence, no raw prose."""
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
from prepare_livedoor_leads import RUN,CONFIG,reference,inspect


def main():
    inspect();destination=ROOT/'reports/phase6/livedoor_leads_preparation_completion.json'
    if destination.exists():raise ValueError('Preserve original news preparation milestone')
    job=read_json(RUN/'job.json');ready=read_json(RUN/'ready.json');review=read_json(RUN/'content-review.json')
    proposal=ROOT/'reports/phase6/livedoor_base_comparison_proposal.json';p=read_json(proposal)
    if (job['status']!='complete' or alive(job) or review['weak_documents']!=8 or not review['passed']
            or p['source_ready']!=reference(RUN/'ready.json') or p['source_content_review']!=reference(RUN/'content-review.json')
            or p['new_scientific_teacher_tokens']+p['reused_prefix_teacher_tokens']!=100000000
            or p['scientific_GPU_frozen'] or p['new_GPU_seconds']):raise ValueError('Actual accepted64 and no-new-GPU shared-prefix definition required')
    report=dict(status='authored_news_source_ready_and_shared_Web_prefix_defined',created_at=now(),actual_job=job,
        ready=reference(RUN/'ready.json'),actual_ready=ready,content_review=reference(RUN/'content-review.json'),
        weak_documents=8,maximum_weak_documents=10,all64_individually_read=True,independent_human_blind=False,
        comparison_proposal=reference(proposal),actual_proposal=p,original_UI=original_UI(),
        GPU_seconds=0,scientific_teacher_tokens=0,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        raw_checksum_attestation='Local SHA256 of actual downloaded archive bytes, not a publisher-signed checksum or independently certified corpus.',
        raw_articles_sample64_and_binary_shards_native_only=True,old_Web_cross_corpus_audit_complete=False,
        next_action='Implement native inherited-state exact two-source teacher quota sampler/trainer; own CUDA4vs2+2/32timing and measured total<=1800 before science freeze. Common native Web prefix73,571,878 reused; new26,428,122 targets include Web1,428,122+news25M. Full100M total exposure and reused/new/input budgets distinct.')
    atomic_json(destination,report)
    names=('scripts/prepare_livedoor_leads.py','scripts/review_livedoor_leads.py','scripts/define_livedoor_base_comparison.py',
        'scripts/record_livedoor_preparation.py','scripts/analyze_readout_source_stages.py','tests/test_livedoor_leads.py','tests/test_readout_source_stages.py',
        'reports/phase6/livedoor_leads_tests.xml','reports/phase6/livedoor_leads_observations.tsv','reports/phase6/livedoor_leads_content_review.json',
        'reports/phase6/readout_source_stage_analysis.json','reports/phase6/readout_source_stages_tests.xml')
    files=[destination,CONFIG,proposal,*[ROOT/n for n in names],RUN/'job.json',RUN/'ready.json',RUN/'content-review.json']
    archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for q in files:output.add(q,arcname=q.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={q.relative_to(ROOT).as_posix():dict(bytes=q.stat().st_size,sha256=sha256(q)) for q in files},
        file_count=len(files),archive=reference(archive),raw_training_material_native_only=True))
    detail=(f'前turn出力変換100M/全80は2dfea0aで不採用。今回同3068/100M全paired TRAIN historyをCPU.098275秒で分析し、末尾32のCEは4sourceともnativeより高い。'
        '事後/fresh readout Adam差/混在境界別会計で、原因や容量不足の証明にしない。'
        f'新[配布者livedoorニュースコーパス](https://www.rondhuit.com/download.html#ldcc)をdownload{ready["download_seconds"]:.6f}秒・CPU{ready["CPU_seconds"]:.6f}秒で準備。'
        '元7367記事→TRAIN5050原first paragraphs/本文523883・BOS/EOS込533983tokens、EOS/教師.009548。'
        'article-ID family90/5/5のdev374/test376本文をdecode/tokenizeせず、local exact127重複を除外。旧Webcross重複/独立audit未完、新規distinctを断定しない。'
        '固定64全個別nonblind採点・弱8<=10でsource受入。医学宣伝/こちら参照/語欠落などの弱い例を記録し、後から除去/rerollせず原5050を保持。'
        'これはsource readinessで全5050監査・モデル品質・独立人手の証明ではない。原archive/LICENSE/全文章/64raw/binaryはnative保存、portableはhash/provenance/notes/codeのみ。'
        f'CPU{p["preparation_CPU_seconds"]:.6f}秒で旧native stagedの最大Web-only保存CP322685を品質参照なしに選び、実weights/Adam2group・LR1e-5/RNG/Webcursor/親d18/全会計と10M tiedを確認。'
        '共通Web73571878教師を再GPUせず、残Web1428122+news25M=26428122新教師・全100Mにする一案。news25Mは約47.265反復で、本文523883を教材量として別記。'
        'source/EOS/多様性・物理input/update数が変わる比較で、量のみ/同targetとは称さない。native core/Tokenizer/decoder/旧cached対照を変更しない。'
        '次は専用2source trainer/会計/実保存再開を実装、ownCUDA120秒/32timing後、1.3margin+300評価+probe全1800秒予測内のみ科学凍結。'
        'newGPU/科学0、元UI確認、Base未完成・完成時通知停止、Chat/量子化なし。')
    prefix='Base専用・日本語ニュースsource準備完了（2026-10-06 JST）。\n\n'+detail+'\n\n元相対・絶対・歴史Web1%品質基準/全旧失敗/数値7/Phase0–3維持。source/selector/epoch/LR/decoder/CP救済sweepなし。WSL uv/local commitのみ/pushなし。以下は過去の履歴。\n\n'
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        q=ROOT/relative;q.write_text(prefix+q.read_text(encoding='utf-8-sig'),encoding='utf-8')
    q=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(q)
    progress.update(status=report['status'],updated_at=now(),next_action=report['next_action'],Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['livedoor_source_preparation']=reference(destination);atomic_json(q,progress)
    print(dict(status=report['status'],portable_files=len(files),GPU_seconds=0))


if __name__=='__main__':main()
