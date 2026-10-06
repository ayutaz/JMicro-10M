"""Own hard-gold replay trainer/adaptor; preserve prior frozen GPU code."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError(f'Expected unique source fragment: {old!r}')
    return text.replace(old, new)


def write(relative, text):
    path = ROOT/relative
    if path.exists():
        raise ValueError(f'Preserve own generated source: {relative}')
    path.write_text(text, encoding='utf-8', newline='\n')


def main():
    core = (ROOT/'scripts/eos_decoupled_web_kl_condition_trainer.py').read_text()
    core = once(core, '"""Inherited staged CE plus immutable-parent Web KL; checkpoint both samplers."""',
        '"""Inherited staged CE plus gold-body Web replay; persist hard targets and mass."""')
    core = once(core, 'from eos_decoupled_web_kl_preservation import POLICY,WebBodyReplay,body_parent_kl',
        'from hard_body_web_replay import POLICY,HardBodyReplay,body_gold_ce')
    core = core.replace('historical_parent_staged_CE_frozen_Web_conditional_non_EOS_KL_100M',
        'historical_parent_staged_CE_parent_mass_weighted_gold_Web_body_replay_100M')
    core = core.replace('WebKLTrainer', 'HardBodyReplayTrainer').replace('WebBodyReplay(', 'HardBodyReplay(')
    core = core.replace('scripts/eos_decoupled_web_kl_condition_trainer.py', 'scripts/hard_body_web_replay_trainer.py')
    core = core.replace('scripts/eos_decoupled_web_kl_preservation.py', 'scripts/hard_body_web_replay.py')
    core = core.replace('KL_policy', 'auxiliary_policy').replace('KL_sources', 'auxiliary_sources')
    core = core.replace('staged-CE-frozen-parent-Web-KL', 'staged-CE-parent-mass-weighted-gold-Web-body-replay')
    core = core.replace('KL_state', 'hard_replay_state').replace('reference_soft_target_body_positions', 'reference_hard_body_target_positions')
    core = core.replace('body_parent_kl(', 'body_gold_ce(').replace('reference_KL_loss', 'reference_body_CE_loss')
    core = core.replace('kl_value', 'replay_value').replace('kl,reference_counts=', 'replay_loss,reference_counts=')
    core = core.replace('kl.backward()', 'replay_loss.backward()').replace('float(kl.detach())', 'float(replay_loss.detach())')
    core = once(core, '        self.reference_non_EOS_teacher_mass=0.',
        '        self.reference_non_EOS_teacher_mass=0.\n        self.reference_hard_body_teacher_tokens=0')
    core = once(core, "                raise ValueError('Separate retained probability mass ledger differs')",
        "                raise ValueError('Separate retained probability mass ledger differs')\n"
        "            if type(self.reference_hard_body_teacher_tokens) is not int or self.reference_hard_body_teacher_tokens!=self.replay.body_positions:\n"
        "                raise ValueError('Measured gold-body hard targets differ from replay positions')")
    core = once(core, "        self.reference_non_EOS_teacher_mass+=reference_counts['non_EOS_teacher_probability_mass']",
        "        self.reference_non_EOS_teacher_mass+=reference_counts['non_EOS_teacher_probability_mass']\n"
        "        self.reference_hard_body_teacher_tokens+=reference_counts['hard_body_teacher_tokens']")
    core = once(core, 'reference_hard_body_target_positions=self.replay.body_positions,',
        'reference_hard_body_target_positions=self.reference_hard_body_teacher_tokens,\n'
        "            combined_hard_teacher_positions=self.supervised_tokens-self.lineage['parent_supervised_tokens']+self.reference_hard_body_teacher_tokens,")
    core = once(core, 'replay=self.replay.state_dict(),non_EOS_teacher_probability_mass=self.reference_non_EOS_teacher_mass))',
        'replay=self.replay.state_dict(),non_EOS_teacher_probability_mass=self.reference_non_EOS_teacher_mass,\n'
        '                hard_body_teacher_tokens=self.reference_hard_body_teacher_tokens))')
    core = once(core, "        self.reference_non_EOS_teacher_mass=extra['non_EOS_teacher_probability_mass']",
        "        self.reference_non_EOS_teacher_mass=extra['non_EOS_teacher_probability_mass']\n"
        "        self.reference_hard_body_teacher_tokens=extra['hard_body_teacher_tokens']")
    write('scripts/hard_body_web_replay_trainer.py', core)
    resident = (ROOT/'scripts/eos_decoupled_resident_web_kl_trainer.py').read_text()
    resident = once(resident, '"""Change only Web input delivery; inherit the tested CE/KL math and grad buffers."""',
        '"""Gold-body replay using the accepted exact resident train Web window."""')
    resident = resident.replace('eos_decoupled_web_kl_condition_trainer', 'hard_body_web_replay_trainer')
    resident = resident.replace('BaseWebKLTrainer', 'BaseHardBodyReplayTrainer').replace('WebKLTrainer', 'HardBodyReplayTrainer')
    write('scripts/hard_body_resident_web_replay_trainer.py', resident)
    print('Own gold-body trainer and resident adaptor prepared; no GPU started')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
