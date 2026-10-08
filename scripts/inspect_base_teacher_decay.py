"""Bounded metadata novelty search and first10000-update scalar decay accounting.

No checkpoint load, training, raw generation review or full metrics/corpus scan.
"""
import hashlib
import json
import math
from pathlib import Path
import re
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src')]
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json

PHASE = ROOT / 'reports/phase6'
OUTPUT = PHASE / 'base_teacher_decay_accounting_20261008.json'
INDEX = PHASE / 'base_experiment_index_20261008.json'
TABLE = PHASE / 'base_learning_decision_table_20261008.json'
# A fixed reference teacher count, motivated by old packed32x1024 input shape.
# Historical valid teachers were not always32768; this is NOT an exact replay
# of historical decay, a quality-derived constant or the AdamW paper's sqrt rule.
REFERENCE_TEACHERS = 32768
TERMS = re.compile(r'weight[ _-]?decay|decoupled|teacher.{0,24}decay|decay.{0,24}teacher|normalized.{0,24}decay', re.I)
NORMALIZED = re.compile(r'teacher[ _-]?(?:normalized|normalization)|(?:normalized|normalization).{0,30}decay|decay.{0,30}(?:normalized|normalization)', re.I)


def main():
    started = time.monotonic()
    if OUTPUT.exists():
        raise ValueError('Preserve completed accounting')

    def check_time():
        if time.monotonic() - started > 30:
            raise TimeoutError('Fixed30-second CPU accounting budget exhausted')

    index, table = read_json(INDEX), read_json(TABLE)
    hits, unavailable, normalized_hits = [], [], []
    for row in index['records']:
        check_time()
        path = ROOT / row['path']
        if not path.is_file() or path.stat().st_size > 1048576:
            unavailable.append(row['path'])
            continue
        raw = path.read_bytes()
        text = raw.decode('utf-8')
        if not TERMS.search(text):
            continue
        value = json.loads(raw)
        match_contexts = [text[max(0, m.start()-100):m.end()+200] for m in TERMS.finditer(text)]
        candidate = dict(path=row['path'], sha256=hashlib.sha256(raw).hexdigest(),
                         snapshot_sha256=row['sha256'], changed_since_snapshot=hashlib.sha256(raw).hexdigest()!=row['sha256'],
                         status=value.get('status'), contexts=match_contexts[:8],
                         number_of_matches=len(match_contexts))
        hits.append(candidate)
        if NORMALIZED.search(text):
            normalized_hits.append(dict(path=row['path'], sha256=candidate['sha256'],
                contexts=[text[max(0,m.start()-100):m.end()+200] for m in NORMALIZED.finditer(text)]))

    history = table['first10000_metrics']
    signature = hashlib.sha256()
    prefix_bytes = total = count = 0
    native_log_decay = normalized_log_decay = 0.
    min_rate, max_rate = math.inf, 0.
    lr_sum = wall_seconds = 0.
    milestones = []
    last = None
    with Path(history['path']).open('rb') as stream:
        for count in range(1, 10001):
            check_time()
            raw = stream.readline()
            if not raw:
                raise ValueError('Original10000-update metrics prefix missing')
            signature.update(raw)
            prefix_bytes += len(raw)
            last = json.loads(raw)
            n, lr = last['CE_targets_this_update'], last['lr']
            if (last['update']!=count or type(n) is not int or n<=0
                    or not 0 < .1*lr < 1 or last['supervised_tokens']!=total+n):
                raise ValueError('Ordered finite positive original committed update required')
            total += n
            log_factor = math.log1p(-.1*lr)
            native_log_decay += log_factor
            normalized_log_decay += log_factor*(n/REFERENCE_TEACHERS)
            effective_rate = -math.expm1(log_factor*(n/REFERENCE_TEACHERS))/lr
            min_rate, max_rate = min(min_rate,effective_rate), max(max_rate,effective_rate)
            lr_sum += lr
            wall_seconds += last['seconds']
            if count in (1, 100, 1000, 5000, 10000):
                milestones.append(dict(update=count, teachers=total, last_update_teachers=n,
                    last_lr=lr, last_effective_weight_decay=effective_rate,
                    native_decay_only_factor=math.exp(native_log_decay),
                    teacher_normalized_decay_only_factor=math.exp(normalized_log_decay)))
    c = table['actual_control_counters']
    if (signature.hexdigest()!=history['prefix_sha256'] or prefix_bytes!=history['prefix_bytes']
            or any(last[k]!=c[k] for k in c)
            or not math.isclose(math.exp(native_log_decay),table['grouping_evidence']['baseline_decoupled_weight_decay_factor'],rel_tol=1e-12)):
        raise ValueError('Original prefix/counters/scalar product differ from retained evidence')
    old = read_json(ROOT / 'configs/phase6/base_10b.json')
    # Actual old plan pins this input shape; do not mistake it for valid targets.
    if not any(isinstance(value,dict) and value.get('batch')==32 and value.get('context')==1024
               for value in old.values()):
        raise ValueError('Historical packed input reference shape differs')
    budget = math.ceil(1.3*wall_seconds+300)
    check_time()
    result = dict(status='bounded_decay_novelty_metadata_and_actual_prefix_accounting_complete', created_at=now(),
        sources={name:dict(path=str(path),sha256=sha256(path)) for name,path in
            [('script',Path(__file__)),('index',INDEX),('existing_table',TABLE),('packed_reference_plan',ROOT/'configs/phase6/base_10b.json')]},
        novelty=dict(index_records=len(index['records']),index_observed_at=index['created_at'],
            skipped_in_index=index['skipped'],unavailable_or_oversized=unavailable,
            reports_with_decay_mentions=hits,explicit_normalized_decay_mentions=normalized_hits,
            limits='Keyword search is a bounded prior-report locator, not proof of global novelty. Inspect related primary reports and post-index results before selecting science. Generic repeated LR decay means learning-rate schedule, not weight decay.'),
        original_metrics_prefix=dict(**history,observed_prefix_sha256=signature.hexdigest(),observed_prefix_bytes=prefix_bytes),
        actual_control_counters=c,
        arithmetic=dict(updates=count,teachers=total,mean_teachers_per_update=total/count,
            reference_teachers=REFERENCE_TEACHERS,reference_scope='Fixed32768 teacher reference motivated by historical packed32x1024 input shape; actual historical valid teachers may be fewer. Not an exact historical-decay reconstruction.',
            native_weight_decay=.1,formula='effective_wd=-expm1((n/32768)*log1p(-lr*0.1))/lr; factor=(1-lr*0.1)^(n/32768)',
            native_decay_only_factor=math.exp(native_log_decay),teacher_normalized_decay_only_factor=math.exp(normalized_log_decay),
            minimum_effective_weight_decay=min_rate,maximum_effective_weight_decay=max_rate,
            sum_learning_rates=lr_sum,milestones=milestones,
            actual_microbatch_wall_seconds=wall_seconds,measured_same_work_pilot_GPU_cap_seconds=budget,
            pilot_budget_limit_seconds=3600,measured_budget_eligible=budget<=3600),
        CPU_seconds=time.monotonic()-started,CPU_cap_seconds=30,GPU_seconds=0,
        new_scientific_teacher_tokens=0,new_ratings=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,
        inference_limits='Scalar multiplicative decay contribution only; learned weights also receive Adam updates. Factors do NOT show that weight norms contracted by these amounts or that decay caused quality failure. Grouping and initialization quality results remain rejected. Not the sqrt normalization of Loshchilov/Hutter; a separate fixed per-teacher exposure convention.',
        next_action='Inspect recorded normalized/related prior-report hits. If no equivalent completed or closed experiment exists, define one native same-stream first10000-update comparison changing only weight decay exposure. Same seed/init/Adam timing/CE/clipping/LR/source/teachers, old control raw/notes reused, own exact resume proof and original quality gates; freeze before any GPU. No coefficient sweep or automatic extension.')
    check_time()
    atomic_json(OUTPUT,result)
    print(json.dumps(dict(status=result['status'],CPU_seconds=result['CPU_seconds'],
        records=len(index['records']),decay_mentions=len(hits),normalized_mentions=normalized_hits,
        arithmetic=result['arithmetic']),ensure_ascii=False,indent=2))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
