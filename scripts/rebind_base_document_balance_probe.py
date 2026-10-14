"""Preserve pre-GPU prototype and create explicit corrected execution contract."""
import hashlib
import json
from pathlib import Path
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]


def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    old = ROOT/'configs/phase6/base_document_balance_probe.json'
    new = ROOT/'configs/phase6/base_document_balance_probe_v2.json'
    report = ROOT/'reports/phase6/base-document-balance-preparation-20261014/prototype_amendment.json'
    if report.exists(): raise ValueError('Preserve completed amendment; no repeat rebinding')
    if (ROOT/'reports/phase6/base-document-balance-probe-20261014/job.json').exists():
        raise ValueError('Cannot amend a launched experiment')
    value = json.loads(old.read_text())
    payload = json.loads(Path(value['payload']['path']).read_text())
    assert payload['original_record']['split'] == 'train'
    assert payload['original_record']['body_tokens'] == 1024
    assert len(payload['window']['input_ids']) == 1024
    assert len(payload['window']['target_ids']) == 1024
    assert sum(n != -100 for n in payload['window']['target_ids']) == 512
    corrected = dict(value)
    corrected['source_sha256'] = {p: digest(ROOT/p) for p in value['source_sha256']}
    corrected['prototype_contract'] = dict(path=old.relative_to(ROOT).as_posix(), sha256=digest(old))
    corrected['execution_revision'] = 2
    report.parent.mkdir(parents=True, exist_ok=True)
    resumed_incomplete_receipt = new.exists()
    if new.exists():
        if json.loads(new.read_text()) != corrected:
            raise ValueError('Existing execution contract differs; cannot overwrite')
    else:
        new.write_text(json.dumps(corrected, indent=2, ensure_ascii=False)+'\n')
    report.write_text(json.dumps(dict(recorded_at=datetime.now(timezone.utc).isoformat(),
        reason='Static schema inspection before GPU found original length in payload.original_record.body_tokens, not payload.window. Use preserved original metadata, identical worst shape and unchanged weighting recipe.',
        old_contract_sha256=digest(old), execution_contract_sha256=digest(new),
        GPU_work_before_amendment=False, scientific_training_before_amendment=0,
        same_recipe=True, same_TRAIN=True, same_screen_and_budgets=True,
        source_snapshot='prototype_v1/probe_base_document_balance.py',
        payload_schema_verified=True,
        recovered_incomplete_preparation_receipt=resumed_incomplete_receipt,
        original_preparation_error='Missing WSL receipt directory after contract write' if resumed_incomplete_receipt else None), indent=2)+'\n')
    print(json.dumps(dict(status='pre_GPU_schema_repair_recorded',execution_contract=str(new),sha256=digest(new))))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
