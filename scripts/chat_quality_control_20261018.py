"""Run the existing public 100-case diagnostic on its matched C0 checkpoint."""
import argparse
import importlib
import shutil
import chat_quality_100 as original

ROOT = original.ROOT
RUN = ROOT / 'reports/phase7/chat-recovery-20261018/control100'
C0 = '55280bf3d14361db1687d0e2471c82f96c6407e4f608c8e6508a2d73effa3a1f'


def configure():
    original.RUN = RUN
    original.CHECKPOINT = C0
    original.URL = 'http://127.0.0.1:7865'


def prepare():
    source = ROOT / 'reports/phase7/chat-quality-100-20261017'
    assert not RUN.exists(), 'Never overwrite an existing execution'
    original.model_info()
    RUN.mkdir(parents=True)
    shutil.copyfile(source / 'cases.json', RUN / 'cases.json')
    p = original.read(source / 'protocol.json')
    p.update(created_at=original.now(), checkpoint_sha256=C0, URL=original.URL,
             original_C1_protocol_sha256=original.sha(source / 'protocol.json'),
             wrapper_sha256=original.sha(__file__),
             scope='New C0 diagnostic only; preserve the completed original C1 condition')
    assert p['cases_sha256'] == original.sha(RUN / 'cases.json')
    original.save(RUN / 'protocol.json', p)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('mode', choices=['prepare', 'run', 'packet', 'review'])
    p.add_argument('--start', type=int, default=0)
    p.add_argument('--count', type=int, default=25)
    a = p.parse_args()
    configure()
    if a.mode == 'prepare':
        prepare()
        return
    assert original.read(RUN / 'protocol.json')['wrapper_sha256'] == original.sha(__file__)
    if a.mode == 'run':
        original.run()
    elif a.mode == 'packet':
        original.packet(a.start, a.count)
    else:
        importlib.import_module('review_chat_quality_100').main()


if __name__ == '__main__':
    main()
