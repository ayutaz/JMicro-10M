"""Own one component-ablation prototype; preserve every earlier frozen source."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT


def once(text,old,new):
    if text.count(old) != 1:
        raise ValueError('Expected unique inherited source fragment')
    return text.replace(old,new)


def write(relative,text):
    path = ROOT/relative
    if path.exists() and path.read_text() != text:
        raise ValueError('Preserve own prototype')
    path.write_text(text,encoding='utf-8',newline='\n')


def main():
    core = (ROOT/'scripts/web_kl_condition_trainer_v2.py').read_text()
    core = core.replace('from web_kl_preservation import POLICY,WebBodyReplay,body_parent_kl',
        'from eos_decoupled_web_kl_preservation import POLICY,WebBodyReplay,body_parent_kl')
    core = core.replace('historical_parent_staged_CE_frozen_Web_KL_100M','historical_parent_staged_CE_frozen_Web_conditional_non_EOS_KL_100M')
    core = once(core,"('scripts/web_kl_condition_trainer_v2.py','scripts/web_kl_preservation.py')",
        "('scripts/eos_decoupled_web_kl_condition_trainer.py','scripts/eos_decoupled_web_kl_preservation.py','scripts/web_kl_preservation.py')")
    core = once(core,'        self.lineage.update(', '        self.reference_non_EOS_teacher_mass=0.\n        self.lineage.update(')
    core = once(core,"        self.update+=1;self.tokens+=x.numel();", "        self.reference_non_EOS_teacher_mass+=reference_counts['non_EOS_teacher_probability_mass']\n        self.update+=1;self.tokens+=x.numel();")
    core = once(core,"            reference_input_tokens=self.replay.physical_input_tokens,", "            reference_non_EOS_teacher_probability_mass=self.reference_non_EOS_teacher_mass,\n            reference_input_tokens=self.replay.physical_input_tokens,")
    core = once(core,"                raise ValueError('Completed CE and reference replay counters differ')", "                raise ValueError('Completed CE and reference replay counters differ')\n            if not math.isfinite(self.reference_non_EOS_teacher_mass) or not 0<=self.reference_non_EOS_teacher_mass<=self.replay.body_positions:\n                raise ValueError('Separate retained probability mass ledger differs')")
    core = once(core,"                teacher_weight_digest=self.teacher_digest,replay=self.replay.state_dict()))", "                teacher_weight_digest=self.teacher_digest,replay=self.replay.state_dict(),non_EOS_teacher_probability_mass=self.reference_non_EOS_teacher_mass))")
    core = once(core,"        self.replay.load_state_dict(extra['replay'])", "        self.replay.load_state_dict(extra['replay'])\n        self.reference_non_EOS_teacher_mass=extra['non_EOS_teacher_probability_mass']")
    write('scripts/eos_decoupled_web_kl_condition_trainer.py',core)
    resident = (ROOT/'scripts/resident_web_kl_trainer.py').read_text().replace('from web_kl_condition_trainer_v2 import', 'from eos_decoupled_web_kl_condition_trainer import')
    write('scripts/eos_decoupled_resident_web_kl_trainer.py',resident)
    test = (ROOT/'tests/test_web_kl_condition_trainer_v2.py').read_text().replace('from web_kl_condition_trainer_v2 import','from eos_decoupled_web_kl_condition_trainer import')
    test = once(test,"    resumed.verify_teacher()", "    assert 0<resumed.reference_non_EOS_teacher_mass<resumed.replay.body_positions\n    assert left['KL_state']['non_EOS_teacher_probability_mass']==a[-1]['reference_non_EOS_teacher_probability_mass']\n    resumed.verify_teacher()")
    write('tests/test_eos_decoupled_web_kl_condition_trainer.py',test)
    print('Own weighted conditional non-EOS KL prototype prepared; no GPU/science started')


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
