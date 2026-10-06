import sys
from pathlib import Path

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from base_label_smoothing_trainer import LabelSmoothingTrainer
from base_label_smoothing_packed import PackedLabelSmoothingTrainer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


def builders(tmp_path):
    pool=tmp_path/'pool';manifest=fixture_pool(pool);original=parent()
    binding=dict(parent={'sha256':'CPU-fixture'},weights_role='verification_only')
    def build(packed=True):
        sampler=OriginalTrainCorpusSampler(pool,manifest,FixtureCodec(),dict(web=7500,textbook=2000,story=500))
        cls=PackedLabelSmoothingTrainer if packed else LabelSmoothingTrainer
        return cls(original,sampler,binding,batch=4,device='cpu')
    return build


def without_timing(row):return {k:v for k,v in row.items() if k not in ('seconds','data_wait_seconds')}


def test_packed_transfer_preserves_every_original_state_and_step_value(tmp_path):
    build=builders(tmp_path);ordinary=build(False)
    expected_rows=[ordinary.step() for _ in range(4)];expected=host(ordinary.state_dict())
    packed=build();rows=[packed.step() for _ in range(4)]
    assert equal_state(expected,host(packed.state_dict()))
    assert all(equal_state(without_timing(a),without_timing(b)) for a,b in zip(expected_rows,rows,strict=True))


def test_packed_transfer_full_save_resume_matches_continuous(tmp_path):
    build=builders(tmp_path);continuous=build()
    expected_rows=[continuous.step() for _ in range(4)];expected=host(continuous.state_dict())
    split=build();rows=[split.step() for _ in range(2)];split.save(tmp_path/'split.pt')
    resumed=build();resumed.load(tmp_path/'split.pt');rows.extend(resumed.step() for _ in range(2))
    assert equal_state(expected,host(resumed.state_dict()))
    assert all(equal_state(without_timing(a),without_timing(b)) for a,b in zip(expected_rows,rows,strict=True))
