"""Acquire pinned public sources and TRAIN-only source identities for plan149.

No corpus payload is parsed by this discovery/acquisition command. RPC zip
directory metadata may be listed; protected dialogue members remain unopened.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
from urllib.request import Request, urlopen
import zipfile

ROOT = Path('/home/aihub_ubuntu/src/japanese-tiny-llm-10m')
DATA = Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-natural-sft-20261017')
RUN = ROOT / 'reports/phase7/chat-natural-sft-20261017'
RPC_PIN = '28d0b6b3865b29cabc26c230a2db37cdf315e937'
RPC_SHA = '2fb4fe5c16e6722a0840fe6924113965cffe0b6b9957e436fdb3886fae2743dc'


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def get_json(url):
    with urlopen(Request(url, headers={'User-Agent': 'JMicro-10M-source-preparation'}), timeout=25) as response:
        body = response.read(8 * 1024 * 1024 + 1)
    if len(body) > 8 * 1024 * 1024:
        raise ValueError('Unexpected metadata size')
    return json.loads(body)


def download(url, path, expected=None, limit=800000000):
    if path.exists():
        if expected is not None and sha(path) != expected:
            raise ValueError('Existing source checksum differs; preserve it')
        return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size, reused=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_suffix(path.suffix + '.part')
    if part.exists():
        raise FileExistsError('Inspect prior partial download before recovery')
    count = 0
    with urlopen(Request(url, headers={'User-Agent': 'JMicro-10M-source-preparation'}), timeout=60) as response, part.open('wb') as output:
        while chunk := response.read(1024 * 1024):
            count += len(chunk)
            if count > limit:
                raise ValueError('Public artifact exceeds acquisition size bound')
            output.write(chunk)
    digest = sha(part)
    if expected is not None and digest != expected:
        raise ValueError('Downloaded source checksum differs; preserve partial')
    part.rename(path)
    return dict(path=str(path), sha256=digest, bytes=count, reused=False)


def main(acquire):
    RUN.mkdir(parents=True, exist_ok=True)
    metadata_path = RUN / 'source_metadata.json'
    if metadata_path.exists():
        metadata = json.loads(metadata_path.read_text())
    else:
        api = get_json('https://huggingface.co/api/datasets/llm-jp/magpie-sft-v1.0')
        metadata = dict(observed_at=now(), magpie_revision=api['sha'],
                        magpie_files=[s['rfilename'] for s in api['siblings']],
                        public_source='llm-jp/magpie-sft-v1.0', RPC_revision=RPC_PIN,
                        source_payload_parsed=False, TEST_body_opened=False,
                        requested_scope='Plan149 steps1-5, user authorized; response cap32 steering before freeze')
        save(metadata_path, metadata)
    print(json.dumps(metadata), flush=True)
    if not acquire:
        return
    receipt_path = RUN / 'acquisition.json'
    if receipt_path.exists():
        raise FileExistsError('Acquisition receipt exists; inspect and reuse it')
    receipt = dict(started_at=now(), files={}, status='acquiring', payloads_parsed=False, TEST_body_opened=False)
    save(receipt_path, receipt)
    try:
        receipt['files']['RPC'] = download(
            f'https://codeload.github.com/nu-dialogue/real-persona-chat/zip/{RPC_PIN}',
            DATA / 'raw/real_persona_chat.zip', RPC_SHA, 80000000)
        save(receipt_path, receipt)
        print('Pinned RPC archive acquired; dialogue payloads still unopened.', flush=True)
        split = json.loads((ROOT / 'data/phase1/processed/split_manifest.json').read_text())
        keep = {}
        for kind in ('train', 'dev', 'test'):
            keep[kind] = sorted(n.split(':', 1)[1] for n in split['splits'][kind] if n.startswith('real_persona_chat:'))
        protected = set(keep['dev']) | set(keep['test'])
        with zipfile.ZipFile(DATA / 'raw/real_persona_chat.zip') as archive:
            members = sorted(n for n in archive.namelist() if '/real_persona_chat/dialogues/' in n and n.endswith('.json'))
        assert set().union(*map(set, keep.values())) <= set(members)
        additional = sorted(set(members) - set().union(*map(set, keep.values())))
        # Reserve new development identities before any dialogue payload read.
        new_dev = {n for n in additional if int(hashlib.sha256(('natural-dev42:' + n).encode()).hexdigest()[:8], 16) % 10 == 0}
        allowed_train = sorted(set(members) - protected - new_dev)
        assert not set(allowed_train) & protected
        save(DATA / 'RPC_allowed_identities.json', dict(revision=RPC_PIN, archive_sha256=RPC_SHA,
             preserved_split=keep, new_dev=sorted(new_dev), train=allowed_train,
             body_read=False, identity_policy='Preserve every old split, reserve10percent additional dialogue IDs as DEV; only allowlisted TRAIN zip members may be opened'))
        receipt['RPC_identity_counts'] = dict(all=len(members), train=len(allowed_train),
                                             old_dev=len(keep['dev']), old_test=len(keep['test']), new_dev=len(new_dev))
        rev = metadata['magpie_revision']
        files = [n for n in metadata['magpie_files'] if n.endswith(('.jsonl', '.json', '.parquet')) and not n.endswith('dataset_infos.json')]
        receipt['magpie_artifact_names'] = files
        save(receipt_path, receipt)
        for name in files:
            receipt['files']['magpie:' + name] = download(
                f'https://huggingface.co/datasets/llm-jp/magpie-sft-v1.0/resolve/{rev}/{name}', DATA / 'raw/magpie' / name)
            save(receipt_path, receipt)
            print('Pinned Magpie artifact acquired: ' + name, flush=True)
        receipt.update(status='complete', completed_at=now(), source_payloads_parsed=False,
                       next_action='TRAIN-only extraction and measured short-answer availability; no recipe frozen yet')
        save(receipt_path, receipt)
    except BaseException as error:
        receipt.update(status='failed', error=repr(error), observed_at=now())
        save(receipt_path, receipt)
        raise


if __name__ == '__main__':
    assert sys.version_info[:3] == (3, 12, 7)
    parser = argparse.ArgumentParser()
    parser.add_argument('--acquire', action='store_true')
    main(parser.parse_args().acquire)
