"""Freeze unseen-source sampling/acceptance before retrieving any new bodies."""
import json
from pathlib import Path
import random
import sys

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,now,sha256
from jmicro.training import atomic_json

OUT=ROOT/'configs/phase6/base_hq_acceptance.json'


def main():
    if OUT.exists():raise ValueError('Preserve predeclared unseen-source contract')
    metadata=ROOT/'reports/phase6/base-hq-feasibility-20261007/repository.json'
    source=ROOT/'reports/phase6/base_hq_source_feasibility.json'
    sample=Path('/home/aihub_ubuntu/jmicro-data/phase6/base-hq-sample-20261007/source-sample.json')
    cal=ROOT/'reports/phase6/base_hq_article_calibration.json'
    s=json.loads(source.read_text());m=json.loads(metadata.read_text());c=json.loads(cal.read_text())
    if sha256(metadata)!=s['metadata']['sha256'] or m['sha']!=s['revision'] or c['original_sample_sha256']!=sha256(sample):
        raise ValueError('Actual metadata/parent calibration binding differs')
    seed=2026100731
    candidates=sorted(x['rfilename'] for x in m['siblings']
        if x['rfilename'].startswith('jpn_Jpan/') and x['rfilename'].endswith('.parquet') and x['rfilename']!=s['first_file'])
    files=sorted(random.Random(seed).sample(candidates,4))
    body_calibration=Path(c['calibration']['path'])
    paths=[metadata,source,sample,cal,body_calibration,ROOT/'reports/phase6/base_hq_source_content_review.json',
        ROOT/'artifacts/phase2/4096/tokenizer.model',ROOT/'scripts/base_hq_article_body.py',
        ROOT/'scripts/inspect_base_hq_acceptance.py',ROOT/'scripts/remote_parquet_ranges.py',ROOT/'uv.lock']
    report=dict(status='frozen_unseen_source_acceptance_before_new_bodies',created_at=now(),
        repository=s['repository'],revision=s['revision'],seed=seed,files=files,rows_per_file=16,
        calibration_sample=str(sample),calibration_bodies=str(body_calibration),
        tokenizer='artifacts/phase2/4096/tokenizer.model',bindings={str(p):sha256(p) for p in paths},
        existing_registry='/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/records.sqlite',
        minimum_body_tokens=64,maximum_body_tokens=8192,remote_wall_limit_seconds=60,CPU_limit_seconds=30,
        remote_byte_limit=100*1024*1024,
        sampling='Four uniform files from pinned564 unseen Japanese files. Seeded uniform row group per file; fixed row permutation. First16 eligible TRAIN URL families per group. Original and extracted-body old indexed exact checks, old URL checks, all calibration families/spans and local families/exact bodies excluded. No outcome reroll or score-based source choice.',
        acceptance=dict(documents=64,maximum_weak=10,minimum_usable=54,
            usable='Every original parent and retained original byte span individually read; generally grammatical2, coherent2, complete source article body with local references understandable and no interrupted last clause, no dominant UI/booking/operation junk. Formal lists/questions/quotes are legitimate; no literal sentence-prefix EOS chunking.',
            method='Nonblind Codex linguistic source review bound to both raw-parent and extracted-span SHA, not independent human or model quality. Record all rejected/weak rows; sampling and extractor stay frozen. Factual claims are not certified.'),
        failure_action='End this fixed extractor branch if fewer than54/64 usable, insufficient candidates, or measured supply cannot support a meaningful diverse pool. Do not reroll failed source families or tune thresholds after unseen content.',
        next_action='Actual bounded retrieval and all64 original/extracted-body content review. On pass, measure supply and protected-family exclusions under explicit CPU/data budgets, then freeze a genuinely new controlled native10M Base data-quality comparison; no small CE/DPO/news recipe continuation.',
        source_accepted=False,new_prepared_training_tokens=0,scientific_teacher_tokens=0,GPU_seconds=0,
        Base_complete=False,Chat_started=False,quantization_started=False,
        quality_targets_unchanged=True,old_numerical7_preserved=True,
        limits='Four chosen files/groups are an inspection, not representative global unique-token supply. Source near-family and fixed-evaluation exclusions are mandatory before learning and currently pending. No whole old-corpus scan or protected test body reading for this source inspection.')
    atomic_json(OUT,report)
    print(dict(files=files,minimum_usable=54,wall_seconds=60,remote_bytes=100*1024*1024,new_training=0))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
